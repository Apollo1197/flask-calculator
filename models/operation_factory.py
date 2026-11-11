from models.operations import *

class OperationFactory:

    @staticmethod
    def get_operation(name):

        operations = {
            "add": AddOperation(),
            "subtract": SubtractOperation(),
            "multiply": MultiplyOperation(),
            "divide": DivideOperation()
        }

        return operations.get(name)


