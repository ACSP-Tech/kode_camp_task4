# Import the function to check and create the necessary file path and JSON file if not already present
from inventory import check_filepath
# Ensure the file path and initial JSON file are set up before running the system
check_filepath()

# Main function for running the Books system
def Books_system():
    # Import menu function and Books class from inventory module
    from inventory import menu, Books
    # Placeholder values to create a Books object (will be overwritten inside the methods)
    title = "placeholder"
    author = "placeholder"
    price = 0
    score = 0
    # Continuous loop to keep system running until user chooses to exit
    while True:
        # Show the menu and get the user-selected option
        option = menu() 
        # If user selects option 1, trigger the add_option method
        if option == 1:
            Books_record = Books(title, author, price, score)
            Books_record.add_option()
        # If user selects option 2, trigger the view_option method
        elif option == 2:
            Books_record = Books(title, author, price, score)
            Books_record.view_option()
        # If user selects option 3, trigger the edit_option method
        elif option == 3:
            Books_record = Books(title, author, price, score)
            Books_record.edit_option()
        # If user selects option 4, trigger the purchase_option method
        elif option == 4:
            Books_record = Books(title, author, price, score)
            Books_record.purchase_option()
        # If user selects option 5, trigger the sales_option method
        elif option == 5:
            Books_record = Books(title, author, price, score)
            Books_record.sales_option()
        # If user selects option 6, exit the loop and end the program
        elif option == 6:
            print("Thanks and bye!!!")
            break
# Call the main system function to start the book inventory application
Books_system()   