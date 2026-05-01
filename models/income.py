from models.transaction import Transaction

class Income(Transaction):
    def apply(self, account):
        account.balance += self.amount