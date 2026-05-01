from models.transaction import Transaction

class Expense(Transaction):
    def apply(self, account):
        account.balance -= self.amount