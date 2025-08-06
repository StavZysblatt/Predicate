from typing import Any, List
from operations.base import Operation

class AndOperation(Operation):
    def __init__(self, operands: List[Operation]):
        self.operands = operands

    def evaluate(self, value: Any) -> bool:
        return all(op.evaluate(value) for op in self.operands) #Calls evaluate for each operand, Returns true if all are true

    @staticmethod
    def from_dict(operation_dict:dict) -> "AndOperation":
        if operation_dict.get("type") != "and":
            raise ValueError("Invalid operation type for AndOperation")

        operand_dicts = operation_dict.get("operands")

        if not isinstance(operand_dicts, list):
            raise TypeError("AndOperation expects a list of operands")

        operands = [Operation.from_dict(op) for op in operand_dicts]

        return AndOperation(operands)

class OrOperation(Operation):
    def __init__(self, operands: List[Operation]):
        self.operands = operands

    def evaluate(self, value: Any) -> bool:
        return any(op.evaluate(value) for op in self.operands)

    @staticmethod
    def from_dict(operation_dict:dict) -> "OrOperation":
        if operation_dict.get("type") != "or":
            raise ValueError("Invalid operation type for OrOperation")

        operand_dicts = operation_dict.get("operands")

        if not isinstance(operand_dicts, list):
            raise TypeError("OrOperation expects a list of operands")

        operands = [Operation.from_dict(op) for op in operand_dicts]

        return OrOperation(operands)

class NotOperation(Operation):
    def __init__(self, operand: Operation):
        self.operand = operand

    def evaluate(self, value: Any) -> bool:
        return not self.operand.evaluate(value)

    @staticmethod
    def from_dict(operation_dict:dict) -> "NotOperation":
        if operation_dict.get("type") != "not":
            raise ValueError("Invalid operation type for NotOperation")

        operand_dict = operation_dict.get("operand")
        if not isinstance(operand_dict, dict):
            raise TypeError("NotOperation expects a single operation object")

        operand = Operation.from_dict(operand_dict)

        return NotOperation(operand)