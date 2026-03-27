# Build a Text Cleaner

import string

# Sample input text
text = input("Enter a sentence: ")

# Step 1: Convert to lowercase
text = text.lower()

# Step 2: Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 3: Remove stopwords
stopwords = ["is", "the", "and", "in", "to", "of", "a", "this", "that"]

words = text.split()
cleaned_words = []

for word in words:
    if word not in stopwords:
        cleaned_words.append(word)

# Join cleaned words
cleaned_text = " ".join(cleaned_words)

# Output
print("\nCleaned Text:")
print(cleaned_text)