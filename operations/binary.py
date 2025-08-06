from typing import Any
from operations.base import Operation

class EqToOperation(Operation):

    def __init__(self, target: Any):
        self.target = target

    def evaluate(self, value: Any) -> bool:
        return value == self.target

    @staticmethod
    def from_dict(operation_dict:dict) -> "EqToOperation":
        if operation_dict.get("type") != "eqTo":
            raise ValueError("Invalid operation type for eqTo")

        target = operation_dict.get("value")

        return EqToOperation(target)

class NotEqToOperation(Operation):
    def __init__(self, target: Any):
        self.target = target

    def evaluate(self, value: Any) -> bool:
        return value != self.target

    @staticmethod
    def from_dict(operation_dict:dict) -> "NotEqToOperation":
        if operation_dict.get("type") != "notEqTo":
            raise ValueError("Invalid operation type for notEqTo")

        target = operation_dict.get("value")

        return NotEqToOperation(target)

class GtOperation(Operation):
    def __init__(self, target: Any):
        self.target = target

    def evaluate(self, value: Any) -> bool:
        return value > self.target

    @staticmethod
    def from_dict(operation_dict:dict) -> "GtOperation":
        if operation_dict.get("type") != "gt":
            raise ValueError("Invalid Operation type for gt")

        target = operation_dict.get("value")

        return GtOperation(target)

class LtOperation(Operation):
    def __init__(self, target: Any):
        self.target = target

    def evaluate(self, value: Any) -> bool:
        return value < self.target

    @staticmethod
    def from_dict(operation_dict: dict) -> "LtOperation":
        if operation_dict.get("type") != "lt":
            raise ValueError("Invalid Operation type for lt")

        target = operation_dict.get("value")

        return LtOperation(target)

class GteOperation(Operation):
    def __init__(self, target: Any):
        self.target = target

    def evaluate(self, value: Any) -> bool:
        return value >= self.target

    @staticmethod
    def from_dict(operation_dict: dict) -> "GteOperation":
        if operation_dict.get("type") != "gte":
            raise ValueError("Invalid Operation type for gte")

        target = operation_dict.get("value")

        return GteOperation(target)

class LteOperation(Operation):
    def __init__(self, target: Any):
        self.target = target

    def evaluate(self, value: Any) -> bool:
        return value <= self.target

    @staticmethod
    def from_dict(operation_dict: dict) -> "LteOperation":
        if operation_dict.get("type") != "lte":
            raise ValueError("Invalid Operation type for lte")

        target = operation_dict.get("value")

        return LteOperation(target)

class InOperation(Operation):
    def __init__(self, target: Any):
        self.target = target

    def evaluate(self, value: Any) -> bool:
        return value in self.target

    @staticmethod
    def from_dict(operation_dict:dict) -> "InOperation":
        if operation_dict.get("type") != "in":
            raise ValueError("Invalid Operation type for in")

        target = operation_dict.get("value")

        if not isinstance(target,(list, set, tuple)):
            raise TypeError("Target for 'in' must be a list, set or tuple")

        return InOperation(target)

class NotInOperation(Operation):
    def __init__(self, target: Any):
        self.target = target

    def evaluate(self, value: Any) -> bool:
        return value not in self.target

    @staticmethod
    def from_dict(operation_dict: dict) -> "NotInOperation":
        if operation_dict.get("type") != "notIn":
            raise ValueError("Invalid Operation type for notIn")

        target = operation_dict.get("value")

        if not isinstance(target, (list, set, tuple)):
            raise TypeError("Target for 'notIn' must be a list, set or tuple")

        return NotInOperation(target)