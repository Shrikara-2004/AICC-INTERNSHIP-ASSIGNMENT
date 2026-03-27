# House Price Predictor using Kaggle Dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Step 1: Load dataset from Kaggle
data = pd.read_csv("train.csv")

# Step 2: Select useful columns
# Using GrLivArea (Above ground living area) to predict SalePrice
X = data[['GrLivArea']]
y = data['SalePrice']

# Step 3: Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Step 4: Create Linear Regression model
model = LinearRegression()

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Predict price for new house size
size = float(input("Enter house size in square feet: "))
predicted_price = model.predict([[size]])
print("Predicted House Price:", predicted_price[0])
