class Bankaccount():
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amount):
        if amount<=0:
            raise ValueError("Deposit must be +ve")
        self.balance +=amount

    def withdraw(self,amount):
        if amount>self.balance:
            raise ValueError("Insufficient balance")
        self.balance -=amount
    def get_balance(self):
        return self.balance
    