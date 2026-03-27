# Data Doctor - Dataset Cleaning
import pandas as pd

# Step 1: Load dataset
data = pd.read_csv("data.csv")
print("Original Dataset:")
print(data.head())

# Step 2: Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Step 3: Handle missing values (fill with mean for numeric columns)
data.fillna(data.mean(numeric_only=True), inplace=True)

# Step 4: Remove duplicate rows
data.drop_duplicates(inplace=True)

# Step 5: Standardize text (convert to lowercase)
for column in data.select_dtypes(include='object').columns:
    data[column] = data[column].str.lower().str.strip()
print("\nCleaned Dataset:")
print(data.head())
