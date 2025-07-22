def check_filepath():
    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    try:
        import json
        budget_objects = {
            "date" : [],
            "category" : [],
            "amount" : []
        }
        file_path1 = os.path.join(BASE_DIR, "expenses.json")
        if not os.path.exists(file_path1):
            with open(file_path1, "x") as file:
                json.dump(budget_objects, file)
        else:
            print("json file called Books already exits")
            print()
    except Exception as e:
        print(f"Error with the code: {e}")


def menu():
    username = input("Enter your organization name to sign in; \n").strip().upper()
    print(".........)....................................................")
    print()
    print("...     Welcome to your Personal Budget Tracker     ......")
    print("...    Enter a valid interger from the menu options below....")
    num = 1
    menulist = ["Add_budget", "View_budget", "edit_budget", "groupby_category",  "exit"]
    for menu in menulist:
        print()
        print(f"{num}. {menu}")
        print()
        num += 1
    while True:
        try:
            options = int(input("Enter:  \n"))
            if options > 5:
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
        






# Task 3: Personal Budget Tracker

# Goal: Track and categorize expenses.

# Features:

# - Transaction class: date, category, amount

# - Use datetime, json, os modules

# - Group by category, calculate totals

# - Create budget_utils.py for calculations

# - Include a clear README.md

# - Push to GitHub with multiple commits