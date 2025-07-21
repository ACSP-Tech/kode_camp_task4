from models import check_filepath

check_filepath()

def Student_system():
    from models import menu, Student
    name = "placeholder"
    subjects = "placeholder"
    scores = 0
    average = 0
    grade = "placeholder"
    while True:
        option = menu()
        if option == 1:
            student_record = Student(name, subjects, scores, average, grade)
            student_record.add_option()
        elif option == 2:
            student_record = Student(name, subjects, scores, average, grade)
            student_record.view_option()
        elif option == 3:
            student_record = Student(name, subjects, scores, average, grade)
            student_record.update_option()
        elif option == 4:
            print("Thanks and bye!!!")
            break



Student_system()
