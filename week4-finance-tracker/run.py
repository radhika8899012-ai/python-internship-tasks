# Personal Finance Tracker
# Week 4 Python Internship Project

import json
import csv
import os
from datetime import datetime

DATA_FILE = "expenses.json"

expenses = []
budgets = {}


def load_data():
    global expenses, budgets

    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)
                expenses = data.get("expenses", [])
                budgets = data.get("budgets", {})
        except (json.JSONDecodeError, OSError):
            print("Error reading data file.")


def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump({
            "expenses": expenses,
            "budgets": budgets
        }, file, indent=4)


def add_expense():
    title = input("Expense name: ").strip()

    if not title:
        print("Name cannot be empty!")
        return

    try:
        amount = float(input("Amount: "))
        if amount <= 0:
            print("Amount must be positive!")
            return
    except ValueError:
        print("Please enter a valid amount!")
        return

    category = input("Category: ").strip().title()

    if not category:
        print("Category cannot be empty!")
        return

    expense = {
        "id": max([e["id"] for e in expenses], default=0) + 1,
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_data()
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    for item in expenses:
        print(item)


def delete_expense():
    view_expenses()

    try:
        expense_id = int(input("Enter expense ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    for item in expenses:
        if item["id"] == expense_id:
            expenses.remove(item)
            save_data()
            print("Expense deleted!")
            return

    print("Expense not found.")


def edit_expense():
    view_expenses()

    try:
        expense_id = int(input("Enter expense ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    for item in expenses:
        if item["id"] == expense_id:
            title = input("New name (Enter to skip): ").strip()
            amount = input("New amount (Enter to skip): ").strip()
            category = input("New category (Enter to skip): ").strip()

            if title:
                item["title"] = title

            if amount:
                try:
                    value = float(amount)
                    if value <= 0:
                        print("Amount must be positive!")
                        return
                    item["amount"] = value
                except ValueError:
                    print("Invalid amount!")
                    return

            if category:
                item["category"] = category.title()

            save_data()
            print("Expense updated!")
            return

    print("Expense not found.")


def monthly_report():
    month = datetime.now().strftime("%Y-%m")
    total = 0

    print("\nMONTHLY EXPENSE REPORT")

    for item in expenses:
        if item["date"].startswith(month):
            print(item["title"], "-", item["amount"])
            total += item["amount"]

    print("Total Expense:", total)


def category_report():
    totals = {}

    for item in expenses:
        category = item["category"]
        totals[category] = totals.get(category, 0) + item["amount"]

    print("\nCATEGORY REPORT")

    for category, amount in totals.items():
        print(category, ":", amount)


def set_budget():
    category = input("Enter category: ").strip().title()

    try:
        amount = float(input("Enter monthly budget: "))
        if amount <= 0:
            print("Budget must be positive!")
            return
    except ValueError:
        print("Invalid amount!")
        return

    budgets[category] = amount
    save_data()
    print("Budget saved!")


def export_csv():
    with open("expenses.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["id", "title", "amount", "category", "date"]
        )
        writer.writeheader()
        writer.writerows(expenses)

    print("CSV file created successfully!")


def main():
    load_data()

    while True:
        print("\n===== PERSONAL FINANCE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Edit Expense")
        print("4. Delete Expense")
        print("5. Monthly Report")
        print("6. Category Report")
        print("7. Set Budget")
        print("8. Export CSV")
        print("9. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            edit_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            monthly_report()
        elif choice == "6":
            category_report()
        elif choice == "7":
            set_budget()
        elif choice == "8":
            export_csv()
        elif choice == "9":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
