# 📝 Student Report Card App

A terminal-based Python application for managing student scores, calculating averages, and assigning grades. This app allows you to add, view, and update student records, with data stored locally in a JSON file.

---

## 🎯 Goal

Build a maintainable student report card system with proper Git version control and commit history tracking.

---

## 🧩 Features

- 🎓 **Student Class**: Handles name, subjects, scores, average, and grade
- 💾 **JSON Data Storage**: Load and save all student records persistently
- 🔁 **Functional Operations**:
  - Add new student
  - View all students
  - Update student records
- 📁 **File Management**: Uses `os` to handle data paths
- 📌 **Git Version History**: Track meaningful changes with clear commit messages

---

## 🏗️ Project Structure

student_report_card/
├── models.py # Core logic (Student class, menu, data functions)
├── data.json # Stores student records
├── main.py # Runs the terminal app
├── README.md # Project overview and usage guide
