# KNN Similarity Example
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Example dataset (Movie preference: Action=1, Romance=0)
# Features: [Action rating, Romance rating]
X = np.array([[5, 1],[4, 1],  [1, 5],   [2, 4]])

# Labels: 1 = Likes Action movies, 0 = Likes Romance movies
y = np.array([1, 1, 0, 0])

# Create KNN model
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X, y)

# New user preference
new_user = [[4, 2]]

# Predict recommendation type
prediction = model.predict(new_user)
if prediction == 1:
            print("Recommended: Action Movies")
else:
            print("Recommended: Romance Movies")
