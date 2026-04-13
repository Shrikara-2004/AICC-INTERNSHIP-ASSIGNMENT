# NLP Mini App - Keyword Extractor

import requests
import string
from collections import Counter

# Step 1: Fetch text from internet
url = "https://www.gutenberg.org/files/11/11-0.txt"  # Alice in Wonderland text
response = requests.get(url)
text = response.text[:2000]  # take first 2000 characters

# Step 2: Preprocess text
text = text.lower()
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 3: Remove stopwords
stopwords = ["the", "is", "and", "in", "to", "of", "a", "that", "it", "on"]

words = text.split()
filtered_words = [word for word in words if word not in stopwords]

# Step 4: Find top keywords
word_counts = Counter(filtered_words)
top_keywords = word_counts.most_common(10)

# Step 5: Display results
print("Top Keywords:\n")
for word, count in top_keywords:
    print(word, ":", count)