# Smart Input Program

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your hobby: ")

# Categorizing age
if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior Citizen"

# Printing personalized message
print("\n--- Personalized Message ---")
print(f"Hello {name}!")
print(f"You are classified as a {category}.")
print(f"It's great that you enjoy {hobby}!")
print("Keep pursuing your passion and keep learning!")