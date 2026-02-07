class Calculator:

    def add(self, a, b):
        return a + b


    def subtract(self, a, b):
        return a - b


    def multiply(self, a, b):
        return a * b


    def divide(self, a, b):
        if b == 0:
            raise ValueError("Нельзя делить на ноль!")
        return a / b


    def power(self, a, b):
        return a ** b


    def is_even(self, a):
        return a % 2 == 0
