from django.shortcuts import render
from django.http import JsonResponse
from .apps import SentimentConfig
from .preprocessing import preprocess_text, mystem_lemmatize, score_corrector 

def index(request):
    return render(request, 'sentiment/index.html')

def classify(request):
    review = request.POST["review"]
    preproc_review = preprocess_text(review)
    lemmatize_review = mystem_lemmatize(preproc_review)

    vectorize_review = SentimentConfig.tfidf.transform([lemmatize_review])
    
    score = SentimentConfig.model.predict(vectorize_review)
    score = score_corrector(score)[0]

    sentiment = None
    if score > 6:
        sentiment = "Good"
    else:
        sentiment = "Bad"

    return JsonResponse({
        "sentiment":sentiment,
        "score":str(score)
    })