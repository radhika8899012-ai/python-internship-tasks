class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


account = BankAccount("Radhika", 1000)
account.deposit(500)
account.withdraw(200)
account.display_balance()
