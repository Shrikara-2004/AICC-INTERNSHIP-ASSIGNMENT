# Storytelling with Graphs
import matplotlib.pyplot as plt

# Sample dataset
categories = ['Books', 'Electronics', 'Clothing', 'Food']
sales = [120, 200, 150, 100]

# Bar Chart
plt.figure()
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# Pie Chart
plt.figure()
plt.pie(sales, labels=categories, autopct='%1.1f%%')
plt.title("Sales Distribution")
plt.show()# Histogram
marks = [55, 60, 65, 70, 75, 80, 85, 90, 75, 60, 65, 70]
plt.figure()
plt.hist(marks, bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
