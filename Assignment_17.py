# Decision Tree Classification using Iris Dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
data = pd.read_csv("Iris.csv")

# Step 2: Select features and target
X = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = data['Species']

# Step 3: Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Step 4: Create Decision Tree model
model = DecisionTreeClassifier()

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Make predictions
predictions = model.predict(X_test)

# Step 7: Check accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)