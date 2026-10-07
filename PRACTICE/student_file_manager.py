"""A program that:
Takes a student's name and marks as input.
Saves the information into a file called students.txt.
Reads the file and displays the information.
Use try-except to handle any file-related error.
Use a function for saving the student data."""
def save_student(name, marks):
    with open("students.txt", "w") as file:
        file.write("Student Name: " + name + "\n")
        file.write("Student Marks: " + str(marks) + "\n")
try:
    student_name = input("Enter the student name: ")
    student_marks = float(input("Enter the student marks: "))
    save_student(student_name, student_marks)
    with open("students.txt", "r") as file:
        content = file.read()
        print("\nStudent Information:")
        print(content)
except ValueError:
    print("Please enter the marks correctly.")
except FileNotFoundError:
    print("File does not exist.")