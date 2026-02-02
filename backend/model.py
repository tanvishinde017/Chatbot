import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from .responses import training_data
from config import Config

# Training examples
sentences = []
labels = []

intent_examples = {
    "greeting": ["hello", "hi", "hey"],
    "name": ["who are you", "your name"],
    "python": ["what is python", "python language"],
    "goodbye": ["bye", "exit", "quit"]
}

for intent, examples in intent_examples.items():
    for example in examples:
        sentences.append(example)
        labels.append(intent)

# Vectorization
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Train model
model = MultinomialNB()
model.fit(X, labels)

def get_response(user_input: str) -> str:
    X_test = vectorizer.transform([user_input.lower()])
    probabilities = model.predict_proba(X_test)[0]

    best_prob = max(probabilities)
    predicted_intent = model.classes_[probabilities.argmax()]

    if best_prob < Config.CONFIDENCE_THRESHOLD:
        return random.choice(training_data["fallback"])

    return random.choice(training_data[predicted_intent])
