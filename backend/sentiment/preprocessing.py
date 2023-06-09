from .apps import SentimentConfig
import re
import string
import nltk 
from nltk.tokenize import WordPunctTokenizer
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords")
nltk.download('wordnet')

tokenizer = WordPunctTokenizer()
lemmatizer = WordNetLemmatizer()
stopwords = nltk.corpus.stopwords.words("english")

def preprocess_text(text):
    text = re.sub("<br />", "", text)

    sents = []
    for sent in text.lower().split("."):
        tokens = []
        for word in tokenizer.tokenize(sent):
            if (word not in stopwords) and (word not in string.punctuation) \
                    and (not word.isdigit()):
                tokens.append(word)
        sents.append(" ".join(tokens))
    return " ".join(sents)

def lemmatize(sent):
    lemmatized_tokens = []
    for token in tokenizer.tokenize(sent):
        word = lemmatizer.lemmatize(token)
        lemmatized_tokens.append(word)
    return " ".join(lemmatized_tokens)

def score_corrector(label):
    if label > 3:
        return label + 3
    return label + 1