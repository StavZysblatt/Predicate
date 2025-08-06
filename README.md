# Predicate Evaluation

This project evaluates logical predicates on nested Python objects using a dot-path syntax.

A predicate consists of:
- A feature path (e.g. `.user.age`)
- An operation to apply to that feature (e.g. `gt`, `eqTo`, `in`, etc.)

The system supports:
- Binary operations: `eqTo`, `notEqTo`, `gt`, `lt`, `gte`, `lte`, `in`, `notIn`
- Unary operations: `isNone`, `isNotNone`
- Group operations: `and`, `or`, `not`

## Project Structure

BiocatchPredicate/
├── resolver.py # Resolves nested feature paths
├── predicate.py # Main class to evaluate predicates
├── operations/
│ ├── base.py # Base Operation class and dispatcher
│ ├── binary.py # Binary operations
│ ├── unary.py # Unary operations
│ └── group.py # Logical group operations
