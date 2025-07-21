def check_filepath():
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    try:
        import json
        Book_objects = {
            "title" : [],
            "author" : [],
            "price" : [],
            "stock" : []
        }
        file_path1 = os.path.join(BASE_DIR, "Books.json")
        if not os.path.exists(file_path1):
            with open(file_path1, "x") as file:
                json.dump(Book_objects, file)
        else:
            print("json file called Books already exits")
            print()
    except Exception as e:
        print(f"Error with the code: {e}")

def menu():
    print(".............................................................")
    print()
    print("...     Welcome to your Book report card app  ......")
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

class Book:
    def __init__(self, name, subjects, scores, average, grade):
        self.name = name
        self.subjects = subjects
        self.scores = scores
        self.average = average
        self.grade = grade
