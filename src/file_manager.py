import csv
import os

FILE_PATH = "data/expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_PATH):
        os.makedirs("data", exist_ok=True)
        with open(FILE_PATH, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


def add_expense(expense):
    with open(FILE_PATH, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())


def read_expenses():
    expenses = []
    with open(FILE_PATH, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            expenses.append(row)
    return expenses
