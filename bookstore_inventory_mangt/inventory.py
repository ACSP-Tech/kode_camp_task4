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
    print("...     Welcome to your Bookstore Inventory System     ......")
    print("...    Enter a valid interger from the menu options below....")
    num = 1
    menulist = ["Add_book", "View", "edit_book", "record_purchase",  "record_sales",  "exit"]
    for menu in menulist:
        print()
        print(f"{num}. {menu}")
        print()
        num += 1
    while True:
        try:
            options = int(input("Enter:  \n"))
            if options > 6:
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


class Books:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def add_to_record(self, record_dict):
        record_dict["title"].append(self.title)
        record_dict["author"].append(self.author)
        record_dict["price"].append(self.price)
        record_dict["stock"].append(self.stock)

    def add_option(self):   
        while True:
            try:
                import math
                title = input("Enter the Book title: \n").strip().lower()
                print()
                author = input(f"Enter the author for {title} Book: \n").strip().lower()
                print()
                price_input = float(input(f"Enter {title} by {author} price: \n").strip())
                price = math.floor(price_input * 100 + 0.5) / 100
                print()
                stock = int(input(f"Enter  an Integer for opening quantity for {title} by {author}: \n"))
                if price <= 0:
                    print("the price can't be less than or equals to Zero")
                    print()
                    continue
                elif stock < 0:
                    print("the opening quantity has to be 0 or above to add items")
                    print()
                    continue  
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            import json
            import os
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(BASE_DIR, "Books.json")
            with open(file_path, "r") as file:
                old_json = json.load(file)  
            #create an Book object
            Book_objects = Books(title, author, price, stock)
            #add Book to the object 
            Book_objects.add_to_record(old_json)
            with open(file_path, "w") as file:
                json.dump(old_json, file)
                print(f"{title} by {author} sucessully added to the Inventory!")
            repeat = input("would you like to add another record for the same Book or a different Book \nType(yes or no) \n")
            if repeat == "yes":
                continue
            else:
                break

    def view_option(self):   
        while True:
            try:
                print()
                option = input("Would you like to view books by a particular author(search) or all \n \nEnter search or all \n").strip().lower()
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            else:
                if option == "search":
                    try:
                        author_name = input("Enter the Specific author name to pull up all books by the author: \n").strip().lower()
                    except Exception as e:
                        print(f"Error with the code: {e}")
                        continue
                    else:
                        import json
                        import os
                        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                        file_path = os.path.join(BASE_DIR, "Books.json")
                        with open(file_path, "r") as file:
                            old_json = json.load(file)
                        Book_view = {
                            "title" : [],
                            "author" : [],
                            "price" : [],
                            "stock" : []
                        }
                        for index in range(len(old_json['author'])):
                            if old_json['author'][index] == author_name:
                                Book_view['title'].append(old_json['title'][index])
                                Book_view['author'].append(old_json['author'][index])
                                Book_view['price'].append(old_json['price'][index])
                                Book_view['stock'].append(old_json['stock'][index])
                        import pandas as pd
                        Book_df = pd.DataFrame(Book_view)
                        if Book_df.empty:
                            print()
                            print(f"{author_name} does not exist on the database\n \nPlease enter a valid author name \n")
                            continue
                        else:
                            print()
                            print(Book_df.sort_index())
                            break
                elif option == "all":
                    import json
                    import os
                    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                    file_path = os.path.join(BASE_DIR, "Books.json")
                    with open(file_path, "r") as file:
                        old_json = json.load(file)
                    import pandas as pd
                    Book_df = pd.DataFrame(old_json)
                    df_sorted = Book_df.sort_values(by=["author", "title"], ascending=[True, True])
                    print(df_sorted)
                    break
                else:
                    print()
                    print("please Enter a valid option between search or all")
                    continue

    def edit_option(self):
        while True:
            try:
                print()
                author_name = input("Enter the author name you will like to update \n").strip().lower()
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            else:
                import json
                import os
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(BASE_DIR, "Books.json")
                with open(file_path, "r") as file:
                    old_json = json.load(file)
                book_view = {
                    "title" : [],
                    "author" : [],
                    "price" : [],
                    "stock" : []
                }
                other_view = {
                    "title" : [],
                    "author" : [],
                    "price" : [],
                    "stock" : []
                }
                for index in range(len(old_json['author'])):
                    if old_json['author'][index] == author_name:
                        book_view['title'].append(old_json['title'][index])
                        book_view['author'].append(old_json['author'][index])
                        book_view['price'].append(old_json['price'][index])
                        book_view['stock'].append(old_json['stock'][index])
                    elif old_json['author'][index] != author_name:
                        other_view['title'].append(old_json['title'][index])
                        other_view['author'].append(old_json['author'][index])
                        other_view['price'].append(old_json['price'][index])
                        other_view['stock'].append(old_json['stock'][index])
                import pandas as pd
                book_df = pd.DataFrame(book_view)
                if book_df.empty:
                    print()
                    print(f"{author_name} author does not exist on the database\n \nPlease enter a valid author name \n")
                    continue
                else:
                    print(book_df)
                try:
                    index = int(input("Enter the index number(row number) of the author book item you like to edit e.g 0 \n").strip())
                    num = 1
                    menulist = ["title", "author",  "price", "stock"]
                    for menu in menulist:
                        print()
                        print(f"{num}. {menu}")
                        print()
                        num += 1
                    record = int(input("enter the integer option from the menu above record you would like to update, \n").strip())
                    if record == 2:
                        new_author = input("Enter the new author_name \n").strip().lower()
                        book_view['author'][index] = new_author
                    elif record == 1:
                        new_title = input("Enter the new title \n").strip().lower()
                        book_view['title'][index] = new_title
                    elif record == 3:
                        import math
                        new_price_input = float(input("Enter the new price \n").strip())
                        new_price = math.floor(new_price_input * 100 + 0.5) / 100
                        book_view['price'][index] = new_price
                    elif record == 4:
                        print("WARNING!!! only update stock in cases of inventory reconcilation or reseting the system. \nNote that inventory automatically update through sold and sales and you will lose the current stock tracking if you proceed")
                        proceed = input("WOuld you like to go back to main menu(yes) or continue(no). Enter Yes or no").strip().lower()
                        if proceed == "no":
                            new_stock = input("Enter the new stock \n").strip().lower()
                            book_view['stock'][index] = new_stock
                        elif proceed == "yes":
                            continue
                    else:
                        print("invalid option, Enter integer from 1 to 4")
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
                    file_path = os.path.join(BASE_DIR, "Books.json")
                    with open(file_path, "w") as file:
                        json.dump(new_json, file)
                    repeat = input("would you like to edit another record for the same author or a different author \nType(yes or no) \n").strip().lower()
                    if repeat == "yes":
                        continue
                    else:
                        break

    def purchase_option(self):
        while True:
            try:
                print()
                import json
                import os
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(BASE_DIR, "Books.json")
                with open(file_path, "r") as file:
                    old_json = json.load(file)
                import pandas as pd
                book_df = pd.DataFrame(old_json)
                if book_df.empty:
                    print()
                    print(f"no items exits yet\n \nPlease enter a valid author name \n")
                    continue
                else:
                    print(book_df)
                index = int(input("Enter the index number(row number) of the author book item you like to add purchase e.g 0 \n").strip())
                quantity_purchase = int(input("enter an integer for the quantity purchases, the stock will automically increase by this \n"))
                old_json['stock'][index] += quantity_purchase  
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            else:
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(BASE_DIR, "Books.json")
                with open(file_path, "w") as file:
                    json.dump(old_json, file)
                repeat = input("would you like to add another purchase \nType(yes or no) \n").strip().lower()
                if repeat == "yes":
                    continue
                else:
                    break

    def sales_option(self):
        while True:
            try:
                print()
                import json
                import os
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(BASE_DIR, "Books.json")
                with open(file_path, "r") as file:
                    old_json = json.load(file)
                import pandas as pd
                book_df = pd.DataFrame(old_json)
                if book_df.empty:
                    print()
                    print(f"no items exits yet\n ")
                    continue
                else:
                    print(book_df)
                index = int(input("Enter the index number(row number) of the author book item you like to add sales items e.g 0 \n").strip())
                quantity_sold = int(input("enter an integer for the quantity sold, the stock will automically decrease by this \n"))
                old_json['stock'][index] -= quantity_sold  
            except Exception as e:
                print(f"Error with the code: {e}")
                continue
            else:
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                file_path = os.path.join(BASE_DIR, "Books.json")
                with open(file_path, "w") as file:
                    json.dump(old_json, file)
                repeat = input("would you like to add another purchase \nType(yes or no) \n").strip().lower()
                if repeat == "yes":
                    continue
                else:
                    break