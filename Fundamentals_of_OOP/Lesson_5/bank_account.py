class BankAccount:

    bank_name = "Python National Bank"
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def get_balance(self):
        return self.balance