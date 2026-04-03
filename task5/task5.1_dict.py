# Create a dictionary of student marks
students={
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    "David": 92
}
name = input("Enter the student's name: ")
# Check if the entered name exists in the dictionary
if name in students:
    # If found
    print(f"{name}'s marks: {students[name]}")
else:
    # If not found
    print("Student not found.")