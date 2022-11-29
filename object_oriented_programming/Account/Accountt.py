

class Accountt:

    def __init__(self, name):
        self.balance = 0

        self.name = name

    pass

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def buy_recharge_card(self, amount):
        if amount > self.balance:
            raise ValueError("amount to withdraw cannot be more than balance")
        self.balance -= amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount

    def make_transfer(self, amount, account_number):
        # if amount < self.balance:
            self.balance -= amount
            account_number.deposit(amount)


