# Check if the 'expenses.json' file exists, if not, create it
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
            print("json file called budgets already exits")
            print()
    except Exception as e:
        print(f"Error with the code: {e}")

# Display the menu options to the user and return their choice
def menu():
    print(".............................................................")
    print()
    print(f"...     Welcome to Personal Budget Tracker     ......")
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

# Transaction class handles budget entry operations
class Transaction:
    def __init__(self, category, amount):
        from datetime import datetime
        self.category = category
        self.amount = amount
        self.date = datetime.today().strftime("%Y-%m-%d")

    # Method to add transaction to dictionary
    def add_to_record(self, record_dict):
        record_dict["date"].append(self.date)
        record_dict["category"].append(self.category)
        record_dict["amount"].append(self.amount)

    # Add new budget entry
    def add_option(self):   
        while True:
            try:
                import math
                category = input("Enter the budget category: \n").strip().lower()
                print()
                amount_input = float(input(f"Enter the amount for {category} budget: \n").strip().lower())
                amount = math.floor(amount_input * 100 + 0.5) / 100
                print()
                if amount <= 0:
                    print("the price can't be less than or equals to Zero")
                    print()
                    continue
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            import json
            import os
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(BASE_DIR, "expenses.json")
            with open(file_path, "r") as file:
                old_json = json.load(file)  
            #create an budget object
            budget_objects = Transaction(category, amount)
            #add budget to the object 
            budget_objects.add_to_record(old_json)
            with open(file_path, "w") as file:
                json.dump(old_json, file)
                print(f"{category} with {amount} amount sucessully added to the Inventory!")
            repeat = input("would you like to add another record  \nType(yes or no) \n")
            if repeat == "yes":
                continue
            else:
                break
    
    # View all budget entries
    def view_option(self):   
        while True:      
            import json
            import os
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(BASE_DIR, "expenses.json")
            with open(file_path, "r") as file:
                old_json = json.load(file)
            import pandas as pd
            budget_df = pd.DataFrame(old_json)
            if budget_df.empty:
                print()
                print(f"There is no item in the budget tracker \n")
                break
            else:
                print()
                print(budget_df.sort_index())
                break
    
    # Group transactions by category and show total amount spent per category
    def groupby_option(self):
        while True:
                import json
                import os
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(BASE_DIR, "expenses.json")
                with open(file_path, "r") as file:
                    old_json = json.load(file)
                import pandas as pd
                Book_df = pd.DataFrame(old_json)
                df_grouped = Book_df.groupby("category", as_index=False)["amount"].sum()
                print(df_grouped)
                break

    # Edit a transaction based on category name and index    
    def edit_option(self):
        while True:
            try:
                print()
                category_name = input("Enter the category name you will like to edit \n").strip().lower()
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            else:
                import json
                import os
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(BASE_DIR, "expenses.json")
                with open(file_path, "r") as file:
                    old_json = json.load(file)
                book_view = { 
                    "date" : [],
                    "category" : [],
                    "amount" : []
                }
                other_view = {
                    "date" : [],
                    "category" : [],
                    "amount" : []
                }
                for index in range(len(old_json['category'])):
                    if old_json['category'][index] == category_name:
                        book_view['date'].append(old_json['date'][index])
                        book_view['category'].append(old_json['category'][index])
                        book_view['amount'].append(old_json['amount'][index])
                    elif old_json['category'][index] != category_name:
                        other_view['date'].append(old_json['date'][index])
                        other_view['category'].append(old_json['category'][index])
                        other_view['amount'].append(old_json['amount'][index])
                import pandas as pd
                budget_df = pd.DataFrame(book_view)
                if budget_df.empty:
                    print()
                    print(f"{category_name} category does not exist on the database\n \nPlease enter a valid category name \n")
                    continue
                else:
                    print(budget_df)
                try:
                    index = int(input("Enter the index number(row number) of the budget item you like to edit e.g 0 \n").strip())
                    num = 1
                    menulist = ["category", "amount"]
                    for menu in menulist:
                        print()
                        print(f"{num}. {menu}")
                        print()
                        num += 1
                    record = int(input("enter the integer option from the menu above record you would like to update, \n").strip())
                    if record == 2:
                        import math
                        amount_input = float(input("Enter the new amount \n").strip().lower())
                        new_amount = math.floor(amount_input * 100 + 0.5) / 100
                        book_view['amount'][index] = new_amount
                    elif record == 1:
                        new_category = input("Enter the new category \n").strip().lower()
                        book_view['category'][index] = new_category
                    else:
                        print("invalid option, Enter integer 1 or 2")
                        continue          
                except Exception as e:
                    print(f"Error with the code: {e}")
                    continue
                else:
                    # Convert both to DataFrame
                    new_json = {
                    key: book_view[key] + other_view[key] for key in book_view}
                    import os
                    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                    file_path = os.path.join(BASE_DIR, "expenses.json")
                    with open(file_path, "w") as file:
                        json.dump(new_json, file)
                    repeat = input("would you like to edit another record  \nType(yes or no) \n").strip().lower()
                    if repeat == "yes":
                        continue
                    else:
                        break