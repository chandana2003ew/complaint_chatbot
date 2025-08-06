import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
from nlp.preprocess import clean_text  # make sure this exists

# Load training data (CSV must be in data/complaints.csv)
data = pd.read_csv("data/complaints.csv")  # must have: text, category, priority

# Preprocess the text data
data['clean_text'] = data['text'].apply(clean_text)

# Create TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['clean_text'])

# Train category prediction model
category_model = MultinomialNB()
category_model.fit(X, data['category'])

# Train priority prediction model
priority_model = MultinomialNB()
priority_model.fit(X, data['priority'])

# Save all models
joblib.dump(category_model, "models/category_model.pkl")
joblib.dump(priority_model, "models/priority_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")  # used in prediction

print("✅ Models trained and saved successfully!")
