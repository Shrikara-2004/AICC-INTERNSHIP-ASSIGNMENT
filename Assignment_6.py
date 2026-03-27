# Student Data Manager

students = {}

# Input data for 5 students
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks of {name}: "))
    students[name] = marks

# Calculate class average
total = sum(students.values())
average = total / len(students)

# Find topper
topper = max(students, key=students.get)
top_marks = students[topper]

# Function to assign grade
def assign_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 40:
        return "D"
    else:
        return "F"

# Display results
print("\n--- Student Grades ---")
for name, marks in students.items():
    print(f"{name}: Marks = {marks}, Grade = {assign_grade(marks)}")

print("\n--- Class Summary ---")
print(f"Class Average: {average:.2f}")
print(f"Topper: {topper} with {top_marks} marks")