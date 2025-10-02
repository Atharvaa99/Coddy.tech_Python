class BankAccount:
    interest_rate = 0.02

    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = balance

    def display_info(self):
        print(f"Account: {self.account_holder}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {self.interest_rate*100}%")
        print()