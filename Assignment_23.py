# Movie Review Analyzer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Training data
reviews = [
    "I loved this movie",
    "This film was amazing",
    "I hated this movie",
    "This movie was terrible",
    "It was a fantastic experience",
    "Worst movie ever"
]

# Labels: 1 = Positive, 0 = Negative
labels = [1, 1, 0, 0, 1, 0]

# Step 2: Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# Step 3: Train model
model = MultinomialNB()
model.fit(X, labels)

# Step 4: Test on new reviews
test_reviews = [
    "This movie is awesome",
    "I really hate this film",
    "It was a great movie",
    "Worst experience ever",
    "I enjoyed the movie a lot"
]

X_test = vectorizer.transform(test_reviews)
predictions = model.predict(X_test)

# Step 5: Display results
for review, pred in zip(test_reviews, predictions):
    if pred == 1:
        print(f"Review: {review} -> Positive")
    else:
        print(f"Review: {review} -> Negative")