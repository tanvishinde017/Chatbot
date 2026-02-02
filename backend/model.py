import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from .responses import training_data

# Prepare training dataset
sentences = []
labels = []

intent_examples = {
    "greeting": ["hello", "hi", "hey"],
    "name": ["your name", "who are you"],
    "python": ["what is python", "python language"],
    "goodbye": ["bye", "exit", "quit"]
}

for intent, examples in intent_examples.items():
    for sentence in examples:
        sentences.append(sentence)
        labels.append(intent)

# Vectorizer + Model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

model = MultinomialNB()
model.fit(X, labels)

def get_response(user_input):
    X_test = vectorizer.transform([user_input.lower()])
    intent = model.predict(X_test)[0]
    return random.choice(training_data[intent])
