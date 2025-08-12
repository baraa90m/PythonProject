"""
What is TypeVar?
TypeVar, short for Type Variable, is a powerful feature in Python's typing module that allows you to create
more flexible and dynamic type hints. It enables you to create generic functions and classes, making it possible to
reuse code while maintaining type safety. TypeVar is especially useful when you want to define a function or class
that works with multiple types but still enforce some constraints on those types.
"""

from typing import TypeVar, List

T = TypeVar("T")        # T represents a generic type that can be replaced by any other type when the TypeVar is used.

U = TypeVar("U", int, float)   # In this case, U can only be replaced by either int or float.

V = TypeVar("V", bound = List)  # Here, V can be any type that is a subclass of List.

# Type Hints for Generic Functions
def identity(x: T) -> T:
    return x

# Leveraging TypeVar for Flexible Type Constraints
Number = TypeVar("Number", int, float)

def add(x: Number, y: Number) -> Number:
    return x + y
print(add(5.5,3.2))


"""
Refernces:
1- https://io.traffine.com/en/articles/python-typevar
"""