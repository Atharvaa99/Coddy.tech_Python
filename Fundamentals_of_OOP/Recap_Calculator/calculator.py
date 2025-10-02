class Calculator:
    def __init__(self):
        self.result = 0

    def add(self,number):
        self.result += number
        return self.result

    def subtract(self,number):
        self.result -= number
        return self.result

    def multiply(self,number):
        self.result *= number
        return self.result

    def divide(self,number):
        if number == 0:
            print("Error: Division by zero")

        else:
            self.result /= number
        return self.result

    def clear(self):
        self.result = 0
        return self.result

    def get_result(self):
        return self.result
