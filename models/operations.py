class AddOperation:
    def calculate(self, a, b):
        return a + b


class SubtractOperation:
    def calculate(self, a, b):
        return a - b


class MultiplyOperation:
    def calculate(self, a, b):
        return a * b


class DivideOperation:
    def calculate(self, a, b):
        return a / b if b != 0 else "Error"


