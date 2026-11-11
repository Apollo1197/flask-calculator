class Calculator:

    def __init__(self, operation):
        self.operation = operation

    def execute(self, a, b):
        return self.operation.calculate(a, b)