# 🎓 Grade Management System

> A simple Python-based system for managing students, grades, and academic performance.

This project is part of my **Python learning journey**, focused on practicing functions, dictionaries, lists, loops, and building a complete menu-driven program.

---

## ✨ Features

- 👤 Add new students
- 🆔 Prevent duplicate student IDs
- 📝 Add grades to students
- 📋 View student information and grades
- 📊 Calculate student averages
- ✅ Show passed students
- 🏆 Find the student with the highest average
- ⚠️ Handle students without grades
- 🚪 Interactive command-line menu

---

## 🛠️ Concepts Practiced

- Variables
- Lists
- Dictionaries
- Nested dictionaries
- `for` loops
- `while` loops
- `if / elif / else`
- Functions with `def`
- Parameters and arguments
- `return`
- `input()`
- `append()`
- `sum()`
- `len()`

---

## 🗂️ Data Structure

Student information is stored using a nested dictionary:

```python
students = {
    1001: {
        "name": "Ali",
        "grades": [18, 15, 20]
    },
    1002: {
        "name": "Narges",
        "grades": [17, 19, 20]
    }
}
```

Each student contains:

| Field | Description |
|---|---|
| Student ID | Unique identifier |
| Name | Student's name |
| Grades | List of grades |

---

## 📋 Menu

```text
1. Add student
2. Add grade
3. Show student
4. Show average
5. Show passed students
6. Show highest average
7. Exit
```

---

## ▶️ How to Run

Make sure Python is installed on your computer.

### 1. Clone the repository

```bash
git clone https://github.com/narges-developer/grade-management-system-.git
```

### 2. Open the project folder

```bash
cd grade-management-system-
```

### 3. Run the program

```bash
python "08 - Grade manager functions.py"
```

---

## 🎯 Project Goal

The main goal of this project was to practice **breaking a larger problem into smaller, reusable functions**.

The program separates different responsibilities into individual functions:

```text
Add Student
     ↓
Add Grade
     ↓
Calculate Average
     ↓
Analyze Students
     ↓
Display Results
```

This project helped me practice writing organized and reusable Python code while working with nested dictionaries and lists.

---

## 🚀 Future Improvements

Possible improvements for future versions:

- 🔢 Validate grades between 0 and 20
- 🗑️ Delete students
- ✏️ Edit student information
- 📈 Add more statistics
- 💾 Save student data to a file
- 📂 Load saved data when the program starts
- 🖥️ Build a graphical user interface

---

## 📚 My Python Learning Journey

This project is one of several practical Python projects I am building to strengthen my programming fundamentals and move from **learning syntax → solving problems → building real projects**.

> **Learn → Build → Break → Fix → Improve**