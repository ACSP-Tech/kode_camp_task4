from inventory import check_filepath

check_filepath()

def Books_system():
    from inventory import menu, Books
    title = "placeholder"
    author = "placeholder"
    price = 0
    score = 0
    while True:
        option = menu() 
        if option == 1:
            Books_record = Books(title, author, price, score)
            Books_record.add_option()
            pass
        elif option == 2:
            Books_record = Books(title, author, price, score)
            Books_record.view_option()
        elif option == 3:
            Books_record = Books(title, author, price, score)
            Books_record.edit_option()
        elif option == 4:
            Books_record = Books(title, author, price, score)
            Books_record.purchase_option()
        elif option == 5:
            Books_record = Books(title, author, price, score)
            Books_record.sales_option()
        elif option == 6:
            print("Thanks and bye!!!")
            break
Books_system()   