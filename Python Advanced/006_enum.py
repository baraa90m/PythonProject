"""
An enumeration:

- is a set of symbolic names (members) bound to unique values

- can be iterated over to return its canonical (i.e. non-alias) members in definition order

- uses call syntax to return members by value

- uses index syntax to return members by name

- Enumerations are created either by using class syntax, or by using function-call syntax:
"""

from enum import Enum

# class syntax
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# functional syntax
color = Enum('Color', [('RED', 4), ('GREEN', 2), ('BLUE', 3)])

print(Color.RED.name)
print(Color.RED.value)
print(color.RED.value)