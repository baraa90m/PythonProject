"""
What is super() With __init__() Methods?
The super() function in Python is used to refer to the parent class. When used in conjunction with
the __init__() method, it allows the child class to invoke the constructor of its parent class.
This is especially useful when you want to add functionality to the child class's constructor without
completely overriding the parent class's constructor.
"""

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
# Creating an instance of the Dog class
dog = Dog("Buddy", "Labador")
print(f"My dog's name is {dog.name} and it's breed is {dog.breed}.")


"""
References:
1- https://www.geeksforgeeks.org/python/python-super-with-__init__-method/
"""
