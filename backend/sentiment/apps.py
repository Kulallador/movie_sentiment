from django.apps import AppConfig
import pickle

class SentimentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sentiment'

    model = None
    with open("ml/logreg.pickle", "rb") as f:
        model = pickle.load(f)

    tfidf = None
    with open("ml/tfidf_vectorizer.pickle", "rb") as f:
        tfidf = pickle.load(f)