def check_filepath():
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    try:
        import json
        Student_objects = {
            "name" : [],
            "subjects" : [],
            "scores" : [],
            "average" : [],
            "grade" : []
        }
        file_path1 = os.path.join(BASE_DIR, "Student_record.json")
        if not os.path.exists(file_path1):
            with open(file_path1, "x") as file:
                json.dump(Student_objects, file)
        else:
            print("json file called Student_record already exits")
            print()
    except Exception as e:
        print(f"Error with the code: {e}")

def menu():
    print(".............................................................")
    print()
    print("...     Welcome to your student report card app  ......")
    print("...    Enter a valid interger from the menu options below....")
    num = 1
    menulist = ["Add", "View",  "Update",  "exit"]
    for menu in menulist:
        print()
        print(f"{num}. {menu}")
        print()
        num += 1
    while True:
        try:
            options = int(input("Enter:  \n"))
            if options > 4:
                print("Kindly choose from the option above")
                print()
                continue
            elif options < 1:
                print("Kindly choose from the option above")
                print()
                continue
            else:
                break
        except:
            print("Please Enter a valid Integer")
            print()
            continue
    return options 

class Student:
    def __init__(self, name, subjects, scores, average, grade):
        self.name = name
        self.subjects = subjects
        self.scores = scores
        self.average = average
        self.grade = grade

    def add_to_record(self, record_dict):
        record_dict["name"].append(self.name)
        record_dict["subjects"].append(self.subjects)
        record_dict["scores"].append(self.scores)
        record_dict["average"].append(self.average)
        record_dict["grade"].append(self.grade)


    def add_option(self):   
        while True:
            try:
                name = input("Enter the student name: \n").strip().lower()
                print()
                subjects = input(f"Enter the subject for {name}: \n").strip().lower()
                print()
                scores = float(input(f"Enter {name} score for {subjects} subject: \n"))
                print()
                total = int(input(f"Enter the total score obtainable for {subjects}, \nthis would be used to compute the grade and average \n"))
                if total <= 0:
                    print("total score can't be less that Zero")
                    print()
                    continue
                elif total < scores:
                    print("total score obtainable can't be less than score obtained by student")
                    print()
                    continue  
                print("We would like to personalize the student report card!!! \n \ntherefore, from A to F we would like you to define the grading scale \n \non a scale of 0 percent to 100 percent, answer the following  please do not include the perventage sign e.g (70) for 70 and above \n")
                for i in range(2):
                    a = float(input("enter the percentage cut off for grade A, \n"))
                    b = float(input("enter the percentage cut off for grade b,  \n"))
                    if a < b:
                        print("grade A can't be less than B")
                        continue
                    c = float(input("enter the percentage cut off for grade C,  \n"))
                    if b < c:
                        print("grade C can't be greater than than B")
                        continue
                    d = float(input("enter the percentage cut off for grade D,  \n"))
                    if c < d:
                        print("grade D can't be greater than than C")
                        continue
                    e = float(input("enter the percentage cut off for grade E,  \n"))
                    if d < e:
                        print("grade e can't be greater than than d")
                        continue
                    else:
                        break
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            grade_score = (scores/total) * 100
            if grade_score >= a:
                grade = "A"
            elif grade_score >= b:
                grade = "B"
            elif grade_score >= c:
                grade = "C"
            elif grade_score >= d:
                grade = "D"
            elif grade_score >= e:
                grade = "E"
            else:
                grade = "F"
            import json
            import os
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(BASE_DIR, "Student_record.json")
            with open(file_path, "r") as file:
                old_json = json.load(file)  
            average = total/2 
            #create an Student object
            Student_objects = Student(name, subjects, scores, average, grade)
            #add Student to the object 
            Student_objects.add_to_record(old_json)
            with open(file_path, "w") as file:
                json.dump(old_json, file)
                print(f"{name} sucessully added to report card!")
            repeat = input("would you like to add another record for the same student or a different student \nType(yes or no) \n")
            if repeat == "yes":
                continue
            else:
                break
    
    def view_option(self):   
        while True:
            try:
                print()
                option = input("Would you like to view a student report card or all the student report card record \n \nEnter search(one student) or all(all students) \n").strip().lower()
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            else:
                if option == "search":
                    try:
                        student_name = input("Enter the Specific student name to view the report card: \n").strip().lower()
                    except Exception as e:
                        print(f"Error with the code: {e}")
                        continue
                    else:
                        import json
                        import os
                        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                        file_path = os.path.join(BASE_DIR, "Student_record.json")
                        with open(file_path, "r") as file:
                            old_json = json.load(file)
                        student_view = {
                            "name" : [],
                            "subjects" : [],
                            "scores" : [],
                            "average" : [],
                            "grade" : []
                        }
                        for index in range(len(old_json['name'])):
                            if old_json['name'][index] == student_name:
                                student_view['name'].append(old_json['name'][index])
                                student_view['subjects'].append(old_json['subjects'][index])
                                student_view['scores'].append(old_json['scores'][index])
                                student_view['average'].append(old_json['average'][index])
                                student_view['grade'].append(old_json['grade'][index])
                        import pandas as pd
                        student_df = pd.DataFrame(student_view)
                        if student_df.empty:
                            print()
                            print(f"student name {student_name} does not exist on the database\n \nPlease enter a valid student name \n")
                            continue
                        else:
                            print()
                            print(student_df.sort_index())
                            break
                elif option == "all":
                    import json
                    import os
                    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                    file_path = os.path.join(BASE_DIR, "Student_record.json")
                    with open(file_path, "r") as file:
                        old_json = json.load(file)
                    import pandas as pd
                    student_df = pd.DataFrame(old_json)
                    df_sorted = student_df.sort_values(by=["name", "scores"], ascending=[True, False])
                    print(df_sorted)
                    break
                else:
                    print()
                    print("please Enter a valid option between search or all")
                    continue
    
    def update_option(self):
        while True:
            try:
                print()
                student_name = input("Enter the name of the student you will like to update) \n").strip().lower()
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            else:
                import json
                import os
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(BASE_DIR, "Student_record.json")
                with open(file_path, "r") as file:
                    old_json = json.load(file)
                student_view = {
                    "name" : [],
                    "subjects" : [],
                    "scores" : [],
                    "average" : [],
                    "grade" : []
                }
                other_view = {
                    "name" : [],
                    "subjects" : [],
                    "scores" : [],
                    "average" : [],
                    "grade" : []
                }
                for index in range(len(old_json['name'])):
                    if old_json['name'][index] == student_name:
                        student_view['name'].append(old_json['name'][index])
                        student_view['subjects'].append(old_json['subjects'][index])
                        student_view['scores'].append(old_json['scores'][index])
                        student_view['average'].append(old_json['average'][index])
                        student_view['grade'].append(old_json['grade'][index])
                    elif old_json['name'][index] != student_name:
                        other_view['name'].append(old_json['name'][index])
                        other_view['subjects'].append(old_json['subjects'][index])
                        other_view['scores'].append(old_json['scores'][index])
                        other_view['average'].append(old_json['average'][index])
                        other_view['grade'].append(old_json['grade'][index])
                import pandas as pd
                student_df = pd.DataFrame(student_view)
                if student_df.empty:
                    print()
                    print(f"student name {student_name} does not exist on the database\n \nPlease enter a valid student name \n")
                    continue
                else:
                    print(student_df)
                try:
                    index = int(input("Enter the index number of the the subject you like to update e.g 0 \n").strip())
                    num = 1
                    menulist = ["name", "subjects",  "scores"]
                    for menu in menulist:
                        print()
                        print(f"{num}. {menu}")
                        print()
                        num += 1
                    record = int(input("enter the integer option from the menu above record you would like to update, \n").strip())
                    if record == 1:
                        new_name = input("Enter the new student_name \n").strip().lower()
                        student_view['name'][index] = new_name
                    elif record == 2:
                        new_subject = input("Enter the new subject \n").strip().lower()
                        student_view['subjects'][index] = new_subject
                    elif record == 3:
                        new_scores = float(input("Enter the new score \n").strip())
                        student_view['scores'][index] = new_scores
                        for i in range(2):
                            print("New score automatically update average and grade \n \nyou would need to define the total and grade criteria \n")
                            total = int(input(f"Enter the total score obtainable for the new score you just entered \n").strip())
                            if total <= 0:
                                print("total score can't be less that Zero")
                                print()
                                continue
                            elif total < new_scores:
                                print("total score obtainable can't be less than score obtained by student")
                                print()
                                continue
                            else:
                                break            
                        for i in range(2):
                            a = float(input("enter the percentage cut off for grade A, \n").strip())
                            b = float(input("enter the percentage cut off for grade b,  \n").strip())
                            if a < b:
                                print("grade A can't be less than B")
                                continue
                            c = float(input("enter the percentage cut off for grade C,  \n").strip())
                            if b < c:
                                print("grade C can't be greater than than B")
                                continue
                            d = float(input("enter the percentage cut off for grade D,  \n").strip())
                            if c < d:
                                print("grade D can't be greater than than C")
                                continue
                            e = float(input("enter the percentage cut off for grade E,  \n").strip())
                            if d < e:
                                print("grade e can't be greater than than d")
                                continue
                            else:
                                break
                        grade_score = (new_scores/total) * 100
                        if grade_score >= a:
                            new_grade = "A"
                        elif grade_score >= b:
                            new_grade = "B"
                        elif grade_score >= c:
                            new_grade = "C"
                        elif grade_score >= d:
                            new_grade = "D"
                        elif grade_score >= e:
                            new_grade = "E"
                        else:
                            new_grade = "F"
                        new_average = total/2
                        student_view['grade'][index] = new_grade
                        student_view['average'][index] = new_average
                    else:
                        print("Invalid choice. Please select 1, 2, or 3.")
                        continue
                except Exception as e:
                    print(f"Error with the code: {e}")
                    continue
                else:
                    # Convert both to DataFrame
                    new_json = {
                    key: student_view[key] + other_view[key] for key in student_view}
                    import os
                    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                    file_path = os.path.join(BASE_DIR, "Student_record.json")
                    with open(file_path, "w") as file:
                        json.dump(new_json, file)
                    repeat = input("would you like to update another record for the same student or a different student \nType(yes or no) \n").strip().lower()
                    if repeat == "yes":
                        continue
                    else:
                        break