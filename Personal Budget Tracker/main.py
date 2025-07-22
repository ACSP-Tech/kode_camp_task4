# Import and run the function to ensure the JSON file exists for budget records
from budget_utils import check_filepath
check_filepath()

# Define the main budget system loop
def budget_system():
    from budget_utils import menu, Transaction
    # Initialize default placeholder values
    category = "placeholder"
    amount = 0
    # Infinite loop to continuously display the budget system menu
    while True:
        option = menu() # Display menu and get user selection
        # Option 1: Add a new transaction
        if option == 1:
            Budget_record = Transaction(category, amount)
            Budget_record.add_option()
        # Option 2: View existing transactions
        elif option == 2:
            Budget_record = Transaction(category, amount)
            Budget_record.view_option()
        # Option 3: Edit a transaction
        elif option == 3:
            Budget_record = Transaction(category, amount)
            Budget_record.edit_option()
        # Option 4: Group transactions by category and calculate totals
        elif option == 4:
            Budget_record = Transaction(category, amount)
            Budget_record.groupby_option()
        # Option 5: Exit the budget system
        elif option == 5:
            print("thanks and bye!")
            break
# Run the system
budget_system()