# Build Your First Dataset
import pandas as pd
# Creating dataset
data = {
      "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
      "Marks": [35, 40, 50, 55, 65, 70, 80, 90]
}

dataset = pd.DataFrame(data)
# Display dataset
print("Student Study Dataset:\n")
print(dataset)
# Identify feature and label
feature = dataset["Study_Hours"]
label = dataset["Marks"]
print("\nFeature (Input): Study Hours")
print(feature)
print("\nLabel (Output): Marks")
print(label)
