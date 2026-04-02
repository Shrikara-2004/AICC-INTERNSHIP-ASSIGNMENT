# Word Importance Explorer using TF-IDF

from sklearn.feature_extraction.text import TfidfVectorizer

# Step 1: Create 5 documents
documents = [
    "Machine learning is very useful for data analysis",
    "Data science uses machine learning techniques",
    "Artificial intelligence and machine learning are related fields",
    "Data analysis helps in making better decisions",
    "Learning new technologies is important in modern world"
]

# Step 2: Apply TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Step 3: Get feature names (words)
feature_names = vectorizer.get_feature_names_out()

# Step 4: Display top keywords for each document
for i, doc in enumerate(X):
    print(f"\nDocument {i+1} Top Keywords:")
    
    # Convert to array
    scores = doc.toarray()[0]
    
    # Get top 3 words
    top_indices = scores.argsort()[-3:][::-1]
    
    for idx in top_indices:
        print(feature_names[idx])