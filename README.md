# 💰 Finance Manager (Expense Tracker CLI)

Finance Manager is a command-line based Python application that helps users track, manage, and analyze their daily expenses efficiently.  
It supports adding, viewing, editing, searching, and generating category-wise expense reports using a clean modular architecture.

This project demonstrates **real-world Python development practices**, including file handling, modular design, and CLI-based user interaction.

---

## 🚀 Features

- Add new expenses with date, category, amount, and description
- View all recorded expenses
- Edit existing expenses
- Search expenses by date, category, or description
- Generate category-wise expense reports
- CSV-based persistent storage
- Clean, modular, and scalable code structure

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Storage:** CSV File
- **Interface:** Command Line Interface (CLI)
- **Tools:** VS Code, Git, GitHub

---

## 📂 Project Structure

Finance_Manager/
│
├── main.py # Application entry point
├── requirements.txt # Python dependencies
├── README.md # Project overview
│
├── src/
│ ├── init.py
│ ├── menu.py # CLI menu and user interaction
│ ├── expense.py # Expense data model
│ ├── file_manager.py # CSV read/write operations
│ ├── reports.py # Report generation logic
│ └── utils.py # Validation and helper functions
│
├── data/
│ └── expenses.csv # Expense data file
│
├── tests/
│ └── sample_expenses.csv # Sample data for testing
│
├── docs/
│ └── user_guide.md # Detailed user documentation
│
├── screenshots/ # Application screenshots (optional)
└── venv/ # Virtual environment (ignored in git)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AmanShukla-creator/Finnance_Manager.git
cd Finnance_Manager
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Windows

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Application Menu

--- Finance Manager ---

1. Add Expense
2. View Expenses
3. Edit Expense
4. Search Expense
5. Category Report
6. Exit

## Documentation

```
docs/user_guide.md
```

---

## ⚠️ Known Limitations

1. Uses CSV instead of a database

2. No authentication system

3. Not optimized for very large datasets

## 🔮 Future Enhancements

1. SQLite database integration

2. Monthly and yearly expense reports

3. Expense deletion feature

4. Data visualization (charts & graphs)

5. GUI or Web-based interface

6. Unit testing and CI integration

# 👤 Author

Aman Shukla
GitHub: [AmanShukla-creator](https://github.com/AmanShukla-creator)
