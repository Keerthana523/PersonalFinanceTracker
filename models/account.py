class Account:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_transaction(self, transaction):
        transaction.apply(self)
        self.transactions.append(transaction)