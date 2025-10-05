class BankAccount:
    def __init__(self,account_balance):
        account_balance = 0
        self.account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
        else:
            raise("Deposit amount must be positive.")
    def withdraw(self,amount):
        if amount >0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    def display_balance(self):
        return "Current Balance: $[amount]".replace("[amount]",str(self.account_balance))
