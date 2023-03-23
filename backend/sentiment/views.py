from django.shortcuts import render
from django.http import JsonResponse
from .apps import SentimentConfig
from .preprocessing import preprocess_text, lemmatize, score_corrector 
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'sentiment/index.html')

@csrf_exempt
def classify(request):
    review = request.POST["review"]
    preproc_review = preprocess_text(review)
    lemmatize_review = lemmatize(preproc_review)

    vectorize_review = SentimentConfig.tfidf.transform([lemmatize_review])
    
    score = SentimentConfig.model.predict(vectorize_review)
    score = score_corrector(score)[0]

    sentiment = None
    if score > 6:
        sentiment = "хорошее"
    else:
        sentiment = "плохое"

    return JsonResponse({
        "sentiment":sentiment,
        "score":str(score)
    })