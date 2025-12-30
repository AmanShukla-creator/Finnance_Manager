# 📘 User Guide – Finance Manager

## 1. Introduction

Finance Manager is a command-line based Python application that helps users track and manage their daily expenses.  
Users can add, view, edit, search, and analyze expenses stored in a CSV file.

This project is designed to demonstrate real-world Python project structure, file handling, and modular programming.

---

## 2. System Requirements

- Python 3.8 or higher
- Windows / Linux / macOS
- Terminal or Command Prompt
- No internet connection required

---

## 3. Project Setup

### 3.1 Clone the Repository

`````bash
git clone https://github.com/AmanShukla-creator/Finnance_Manager.git
cd Finnance_Manager

### 3.2 Create virtual Environment
````bash
python -m venv venv

### 3.3 Acitvate Windows
````bash
venv\Scripts\activate

## 4. Run the application
````bash
python main.py

## 5. Application Menu
````bash
--- Finance Manager ---
1. Add Expense
2. View Expenses
3. Edit Expense
4. Category Report
5. Search Expense
6. Exit

## 6. Features and Usage

### 6.1 Add Expense

Allows the user to add a new expense.
Required Inputs:

1. Date (YYYY-MM-DD)
2. Category (e.g., Food, Travel, Birthday)
3. Amount (positive number)
4. Description

The expense is saved automatically in the CSV file.

### 6.2 View Expense

Displays all recorded expenses with:

1. Date
2. Category
3. Amount
4. Description

### 6.3 Edit Expense

Allows modification of an existing expense.

Steps:

1. Select the expense number from the list
2. Enter new values ( leave blank to keep existing values)
3. Expense is updated successfully

### 6.4 Search Expense

Allows searching expenses using keywords.

Search Options:
By Date
By Category
By Description

Matching expenses are displayed instantly.

### 6.5 Category Report

Shows total expenses grouped by category.
````bash
Food: ₹2500
Travel: ₹1200
Birthday: ₹100000

### 6.6 EXIT

## 7. Error Handling

## 8. Conclusion

Finance Manager is a simple yet powerful Python CLI project that demonstrates:

Modular code structure
File handling with CSV
User interaction via terminal
Practical expense management features

````bash

---

## ✅ What this does for you
- ✔ Clean markdown
- ✔ GitHub-ready
- ✔ Looks professional
- ✔ Easy to understand for users & evaluators




`````
