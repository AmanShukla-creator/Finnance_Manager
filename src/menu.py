from .expense import ExpenseData
from .expense import Expense
from .file_manager import add_expense, read_expenses
from .utils import validate_amount
from .reports import category_report

def show_menu():
    while True:
        print("\n--- Finance Manager ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Report")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense_flow()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            category_report(read_expenses())
        elif choice == "4":
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

    expense = Expense(date, category, amount, description)
    add_expense(expense)
    print("✅ Expense added")

def view_expenses():
    expenses = read_expenses()
    print("\nDate | Category | Amount | Description")
    for exp in expenses:
        print(" | ".join(exp))
