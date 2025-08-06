from abc import ABC,abstractmethod
from typing import Any


class Operation(ABC):

    @abstractmethod
    def evaluate(self, value: Any) -> bool:
        pass

    @staticmethod
    def from_dict(operation_dict:dict) -> "Operation":

        from operations.binary import (
            EqToOperation, NotEqToOperation, GtOperation, LtOperation,
            GteOperation, LteOperation, InOperation, NotInOperation
        )
        from operations.group import (
            AndOperation, OrOperation, NotOperation
        )
        from operations.unary import (
            IsNoneOperation, IsNotNoneOperation
        )

        if not isinstance(operation_dict, dict):
            raise TypeError("Operation definition must be in a dictionary")

        if "type" not in operation_dict:
            raise ValueError("Missing 'type' in operation dictionary")

        op_type = operation_dict["type"]

        operation_map = {
            "eqTo": EqToOperation,
            "notEqTo": NotEqToOperation,
            "gt": GtOperation,
            "lt": LtOperation,
            "gte": GteOperation,
            "lte": LteOperation,
            "in": InOperation,
            "notIn": NotInOperation,
            "and": AndOperation,
            "or": OrOperation,
            "not": NotOperation,
            "isNone": IsNoneOperation,
            "isNotNone": IsNotNoneOperation,
        }

        operation_cls = operation_map.get(op_type)

        if operation_cls is None:
            raise ValueError(f"Unsupported operation type: '{op_type}'")

        return operation_cls.from_dict(operation_dict)