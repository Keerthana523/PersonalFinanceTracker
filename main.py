print("PROGRAM STARTED")
from models.account import Account
from models.income import Income
from models.expense import Expense
from services.report_generator import ReportGenerator
from ui.menu import display_menu
from datetime import date

account = Account()
report = ReportGenerator()

while True:
    display_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter income amount: "))
        category = input("Enter category: ")
        account.add_transaction(Income(amt, category, date.today()))

    elif choice == "2":
        amt = float(input("Enter expense amount: "))
        category = input("Enter category: ")
        account.add_transaction(Expense(amt, category, date.today()))

    elif choice == "3":
        report.generate_report(account)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
        