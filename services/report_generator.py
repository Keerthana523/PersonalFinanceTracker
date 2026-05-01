from models.income import Income
from models.expense import Expense

class ReportGenerator:
    def generate_report(self, account):
        income = sum(t.amount for t in account.transactions if isinstance(t, Income))
        expense = sum(t.amount for t in account.transactions if isinstance(t, Expense))

        print("\n--- Report ---")
        print("Total Income:", income)
        print("Total Expense:", expense)
        print("Balance:", account.balance)