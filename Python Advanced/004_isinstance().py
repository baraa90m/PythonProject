"""
Definition and Usage:
The isinstance() function returns True if the specified object is of the specified type, otherwise False.

If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.
"""
x = isinstance("Hello", (float, int, str))
y = isinstance("Hello", (float, int))

print(x)
print(y)



"""
Refernces:
1- https://www.w3schools.com/python/ref_func_isinstance.asp
"""