from typing import Any
from operations.base import Operation

class IsNoneOperation(Operation):

    def evaluate(self, value: Any) -> bool:
        return value is None

    @staticmethod
    def from_dict(operation_dict:dict) -> "IsNoneOperation":

        if operation_dict.get("type") != "isNone":
            raise ValueError("Invalid operation type for IsNoneOperation")

        return IsNoneOperation()

class IsNotNoneOperation(Operation):

    def evaluate(self, value: Any) -> bool:
        return value is not None

    @staticmethod
    def from_dict(operation_dict:dict) -> "IsNotNoneOperation":

        if operation_dict.get("type") != "isNotNone":
            raise ValueError("Invalid operation type for IsNotNone")

        return IsNotNoneOperation()
