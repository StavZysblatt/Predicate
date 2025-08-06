from resolver import resolve_feature_path
from operations.base import Operation
import json

class Predicate:
    def __init__(self, feature: str, operation: dict):
        self.feature = feature
        self.operation = Operation.from_dict(operation)

    def evaluate(self, root: object) -> bool:
        value = resolve_feature_path(root, self.feature)
        return self.operation.evaluate(value)

    @classmethod
    def from_json(cls, json_string: str) -> "Predicate":
        data = json.loads(json_string)
        feature = data.get("feature")
        operation = data.get("operation")
        return cls(feature, operation)
