from models.calculator import Calculator
from models.operation_factory import OperationFactory


class CalculatorController:

    def calculate(self, operation_name, num1, num2):

        operation = OperationFactory.get_operation(operation_name)

        calculator = Calculator(operation)

        return calculator.execute(num1, num2)


