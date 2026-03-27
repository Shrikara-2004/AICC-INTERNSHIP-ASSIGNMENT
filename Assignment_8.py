# Dataset Detective
import pandas as pd

# Step 1: Load dataset
data = pd.read_csv("data.csv")

# Step 2: Display top rows
print("Top 5 rows of dataset:")
print(data.head())

# Step 3: Find column with highest value
highest_column = data.max().idxmax()
print("\nColumn with highest value:", highest_column)

# Step 4: Count missing values
print("\nMissing values in each column:")
print(data.isnull().sum())
