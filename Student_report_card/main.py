# Import check_filepath from models and initialize JSON file if not exists
from models import check_filepath
check_filepath()

# Main function that drives the Student report card system
def Student_system():
    from models import menu, Student  # Import menu function and Student class
    name = "placeholder"
    subjects = "placeholder"
    scores = 0
    average = 0
    grade = "placeholder"
    while True:
        option = menu()  # Display menu and get user option
        if option == 1:
            # Add a new student record
            student_record = Student(name, subjects, scores, average, grade)
            student_record.add_option()
        elif option == 2:
            # View student records (single or all)
            student_record = Student(name, subjects, scores, average, grade)
            student_record.view_option()
        elif option == 3:
            # Update an existing student record
            student_record = Student(name, subjects, scores, average, grade)
            student_record.update_option()
        elif option == 4:
            # Exit the system
            print("Thanks and bye!!!")
            break
        
# Call the system runner        
Student_system()
