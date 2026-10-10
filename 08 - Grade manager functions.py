# ===========================================
# Project: Grade manager
# Description:
# A simple program for grade system.
#
# Concepts Used:
# - Variables
# - List
# - Dictionary
# - for loop
# - while loop
# - Functions (def)
# - if / elif / else
# - input
# - int
# - append
# ===========================================
students = {
    1001: {
        "name": "Ali",
        "grades": [18, 15, 20]
    },
    1002: {
        "name": "Narges",
        "grades": [17, 19, 20]
    },
    1003: {
        "name": "Eva",
        "grades": [13, 16, 18]
    }
}
def add_student():
    new_name = input("Enter student name: ")
    new_id = int(input("Enter student ID: "))
    if new_id in students:
        print("Student ID already exists.")
    else:
        students.update({
        new_id: {
            "name": new_name,
            "grades": []
        }})
        print("Student added successfully.")

def add_grade():
    student_id = int(input("Enter student id: "))
    new_grade = float(input("Enter student grade: "))
    if student_id in students:
        print("Student found!")
        students[student_id]["grades"].append(new_grade)
    else:
        print("Student not found.")

def show_student():
    student_id = int(input("Enter student id: "))
    if student_id in students:
        print("Student found!")
        print("Name:", students[student_id]["name"])
        print("Grades:", students[student_id]["grades"])
        print("------------------")
    else:
        print("Student not found.")
        print("------------------")

def calculate_average(students, student_id):
    num = students[student_id]["grades"]
    if len(num) == 0:
        return 0
    plus = sum(num)
    count = len(num)
    ave = plus / count
    return ave
  
def show_passed_students():
    print("Passed students")
    for student in students:
        if calculate_average(students, student) >= 10:
            print("Student id: ", student, "Name: ", students[student]["name"])

def show_highest_average():
    highest_average = 0
    highest_student = None
    for student in students:
        average = calculate_average(students, student)
        if average > highest_average:
            highest_student = student
            highest_average = average
    print("Student id: ", highest_student, "Name: ", students[highest_student]["name"], "Highest average: ", highest_average)

def show_average():
    student_id = int(input("Enter student id: "))
    if student_id in students:
        print("Student found!")
        ave = calculate_average(students, student_id)
        print("Average: ", ave)
        print("------------------")
    else:
        print("Student not found.")
        print("------------------")

menu = [
    "1. Add student",
    "2. Add grade",
    "3. Show student",
    "4. Show average",
    "5. Show passed students",
    "6. Show highest average",
    "7. Exit"
]

while True:
    for item in menu:
        print(item)
    user_selection = int(input("Enter the number corresponding to your choice: "))    
    if user_selection == 1:
        add_student()
        print("-----------------------")
    elif user_selection == 2:
        add_grade()
        print("-----------------------")
    elif user_selection == 3:
        show_student()
        print("-----------------------")
    elif user_selection == 4:
        show_average()
        print("-----------------------")
    elif user_selection == 5:
        show_passed_students()
        print("-----------------------")
    elif user_selection == 6:
        show_highest_average()
        print("-----------------------")
    elif user_selection == 7:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")