from models.load_models import load_category_model, load_priority_model, load_vectorizer
from nlp.preprocess import clean_text

def analyze_complaint(text):
    clean = clean_text(text)
    vectorizer = load_vectorizer()
    X = vectorizer.transform([clean])

    category_model = load_category_model()
    priority_model = load_priority_model()

    category = category_model.predict(X)[0]
    priority = priority_model.predict(X)[0]

    return category, priority
