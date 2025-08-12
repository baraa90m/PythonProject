"""
Definition and Usage:
- The assert keyword is used when debugging code.
- the assert keyword lets you test if a condition in the code returns True, if not, the program will raise an
 AssertionError.
 - We can write a message to be written if the code returns False, check the example below.
"""

x = "Welcome"

# If condition returns False, AssertionError is raised.
assert x != "Welcome", "x should not be a 'welcome'"