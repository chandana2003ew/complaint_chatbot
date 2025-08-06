import joblib
from nlp.preprocess import clean_text

# Load pre-trained intent classifier and vectorizer
intent_model = joblib.load("models/intent_model.pkl")
vectorizer = joblib.load("models/intent_vectorizer.pkl")

def predict_intent(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    prediction = intent_model.predict(vec)
    return prediction[0]
