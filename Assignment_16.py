# Customer Segmentation using K-Means
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Step 1: Load dataset
data = pd.read_csv("Mall_Customers.csv")

# Step 2: Select important features
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# Step 3: Create K-Means model
kmeans = KMeans(n_clusters=5)

# Step 4: Train the model
data['Cluster'] = kmeans.fit_predict(X)

# Step 5: Visualize clusters
plt.scatter(
 data['Annual Income (k$)'],
data['Spending Score (1-100)'],
c=data['Cluster']
)
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()
