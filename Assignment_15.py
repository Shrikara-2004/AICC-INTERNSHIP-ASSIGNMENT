# Spam Classifier using Kaggle SMS Spam Dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Load dataset
data = pd.read_csv("spam.csv", encoding='latin-1')

# Keep only useful columns
data = data[['v1', 'v2']]
data.columns = ['label', 'message']

# Step 2: Convert labels to numbers
data['label'] = data['label'].map({'ham':0, 'spam':1})

# Step 3: Split dataset
X_train, X_test, y_train, y_test = train_test_split(data['message'], data['label'], test_size=0.2)

# Step 4: Convert text to numbers
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Step 5: Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Step 6: Test with new message
msg = input("Enter a message: ")
msg_vec = vectorizer.transform([msg])
prediction = model.predict(msg_vec)
if prediction[0] == 1:
 print("This message is SPAM")
else:
    print("This message is NOT SPAM")
