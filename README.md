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

1. resolver.py # Resolves nested feature paths
2. predicate.py # Main class to evaluate predicates
3. operations/ 
  a. base.py # Base Operation class
  b. binary.py # Binary operations
  c. unary.py # Unary operations
  d. group.py # Logical group operations
