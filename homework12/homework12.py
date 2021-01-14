import uuid
from datetime import datetime

class Bank_accaunt:
    def __init__(self, name):
        self.name = name
        self.acc_id = uuid.uuid4()
        self.balance = 0.00
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount + (amount * 0.01)
        self.transactions.append((amount, 'deposit', datetime.now().strftime('%d %m %Y')))
        print(self.balance, self.transactions)

    def withdrawal(self, amount):
        self.balance -= amount + (amount * 0.01)
        self.transactions.append((amount, 'withdrawal', datetime.now().strftime('%d %m %Y')))
        print(self.balance, self.transactions)
    def check_bal(self):
        return self.balance

accaunt = Bank_accaunt('accaunt')
accaunt.deposit(200)
accaunt.check_bal()
accaunt.withdrawal(200)
accaunt.check_bal()

