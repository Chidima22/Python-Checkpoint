class Account:
    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = (account_number)
        self.account_balance = float(account_balance)
        self.account_holder = (account_holder)

    def __str__(self):
        return f"Account number: {self.account_number}\nAccount balance: {self.account_balance}\nAccount holder: {self.account_holder}"

    def deposit(self, amount):
        self.account_balance += amount
        return f"Your new account balance is {self.account_balance}"

    def withdraw(self, amount):
        if amount > self.account_balance:
            return "Insuficient Funds"
        else:
            self.account_balance -= amount
            return f"Your new account balance is {self.account_balance}"

    def check(self):
         return f"Your account balance is {self.account_balance}"

# define deposit, withdraw, check balance
# create an instance of the class
# deposit some money
# withdraw some money
# check balance
account1 = Account(account_number="1234567890", account_balance=1000, account_holder="Chidi")
print(account1)
print(account1.deposit(3000))
print(account1.withdraw(900))
print(account1.check())
