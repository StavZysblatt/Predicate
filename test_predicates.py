from types import SimpleNamespace
from predicate import Predicate

json_str_2 = '''
{
  "feature": ".a.b",
  "operation": {
    "type": "and",
    "operands": [
      {"type": "isNotNone"},
      {"type": "eqTo", "value": 15},
      {"type": "lt", "value": 20}
    ]
  }
}
'''

predicate_2 = Predicate.from_json(json_str_2)
obj_3 = SimpleNamespace(a=SimpleNamespace(b=15))
obj_4 = SimpleNamespace(a=SimpleNamespace(b=None))
obj_5 = SimpleNamespace(a=SimpleNamespace(b=25))

print(predicate_2.evaluate(obj_3))
print(predicate_2.evaluate(obj_4))
print(predicate_2.evaluate(obj_5))