from .expense import ExpenseData
from .file_manager import add_expense, read_expenses, write_expenses
from .utils import validate_amount
from .reports import category_report

def show_menu():
    while True:
        print("\n--- Finance Manager ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Report")
        print("4. Edit Expense")
        print("5. Search Expenses")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense_flow()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_report(read_expenses())
        elif choice == "4":
            edit_expense()
        elif choice == "5":
            search_expenses()
        elif choice == "6":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")

def add_expense_flow():
    date = input("Date (YYYY-MM-DD): ")
    category = input("Category: ")
    amount = validate_amount(input("Amount: "))
    if amount is None:
        return
    description = input("Description: ")
    time = input("Time (HH:MM): ")

    expense = ExpenseData(date, category, amount, description, time)
    add_expense(expense)
    print("✅ Expense added")

def view_expenses():
    expenses = read_expenses()
    print("\nDate | Category | Amount | Description")
    for exp in expenses:
        print(" | ".join(exp))
        
def edit_expense():
    expenses = read_expenses()
    if not expenses:
        print("No expense to Edit")
        return

    print("\n _____EXPENSES_____ ")
    for idx, exp in enumerate(expenses, start=1):
        print(f"{idx}. {exp[0]} | {exp[1]} | {exp[2]} | {exp[3]}")

    try:
        choice = int(input("Select expense number to edit: "))
        if choice < 1 or choice > len(expenses):
            print("❌ Invalid choice")
            return
    except ValueError:
        print("Enter a valid number")
        return
    
    date = input("New Date (YYYY-MM-DD): ")
    category = input("New Category: ")
    amount = validate_amount(input("New Amount: "))
    if amount is None:
        return
    description = input("New Description: ")

    if date:
        expenses[choice - 1][0] = date
    if category:
        expenses[choice - 1][1] = category
    if amount:
        expenses[choice - 1][2] = amount
    if description:
        expenses[choice - 1][3] = description

    write_expenses(expenses)
    print("✅ Expense updated")
    
def search_expenses():
    expenses = read_expenses()
    keyword = input("Enter keyword to search: ").lower()
    results = [exp for exp in expenses if keyword in " ".join(exp).lower()]

    if results:
        print("\nSearch Results:")
        for exp in results:
            print(" | ".join(exp))
    else:
        print("No matching expenses found.")