"""
Python classmethod() Function:
In Python, the classmethod() function is used to define a method that is bound to the class
and not the instance of the class. This means that it can be called on the class itself
rather than on instances of the class. Class methods are useful when you need to work with
the class itself rather than any particular instance of it.
"""

class Geeks:
    course = 'DSA'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        Geeks.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome to Geeks for Geeks!"

# Creating instances
g1 = Geeks('Alice')
g2 = Geeks('bob')

# Calling class methods
print(Geeks.get_course())
print(Geeks.get_instance_count())

# Calling static method
print(Geeks.welcome_message())


"""
Hint: Though classmethod and staticmethod are quite similar, there's a slight difference in usage for both entities:
classmethod must have a reference to a class object as the first parameter,
whereas staticmethod can have no parameters at all.

Refernces: 
1- https://www.geeksforgeeks.org/python/classmethod-in-python/
"""