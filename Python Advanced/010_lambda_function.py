"""
- A lambda function is a small anonymous function.
- A lambda function can take any number of arguments, but can only have one expression.
"""

# Example1
x = lambda a: a + 10
print(x(5))


# Example2
x = lambda a, b: a * b
print(x(2,3))

# Example3
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(3))
"""
Refernces:
1- https://www.w3schools.com/python/python_lambda.asp
2- https://www.geeksforgeeks.org/python/python-lambda/
"""