"""
What is serialization and deserialization?
Serialization: is the process of converting an object into a format that can be stored or transmitted,
such as a byte stream or a string.
Deserialization: is the process of reconstructing the object from its serialized form
"""


import pickle

class Person1:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

    def __setstate__(self, state):
        self.name = state["name"]
        self.age = state["age"]

# Example Person1:
person1 = Person1()
person1.__setstate__({"name": "Baraa", "age": 23})
#print(person1.name, person1.age)

#---------------------------------------------------------------------------------
class Person2:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

    def __getstate__(self):
        return {"name": self.name, "age": self.age}


# Example Person 2:
person2 = Person2()
#print(person2.__getstate__())

#---------------------------------------------------------------------------------

class Person3:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

    def __setstate__(self, state):
        self.name = state["name"]
        self.age = state["age"]

    def __getstate__(self):
        return {"name": self.name, "age": self.age}


# Example Person3
person3 = Person3("Max Musterman", 20)
serialized = pickle.dumps(person3)                   # Serialize the object
deserialized = pickle.loads(serialized)              # Deserialized the object
#print(deserialized.name)
#print(deserialized.age)

#---------------------------------------------------------------------------------

class Person4:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __getstate__(self):
        state = self.__dict__.copy()
        state["age"] = state["age"]  +  10           # Increment age by 10 before pickling
        return state

    def __setstate__(self, state):
        state["age"] = state["age"]  - 5           # Decrement age by 10 after unpickling
        self.__dict__.update(state)

# Example Person4
person4 = Person4("Max", 20)
print(person4.age)
pickle_data = pickle.dumps(person4)

new_person = pickle.loads(pickle_data)
#print(new_person.age)

#---------------------------------------------------------------------------------

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __getstate__(self):
        state = self.__dict__.copy()
        state["title"] = state["title"].upper()           # Convert title to uppercase before pickling

        return state
    def __setstate__(self, state):
        state["title"] = state["title"].lower()          # Convert title to lowercase after pickling
        self.__dict__.update(state)

# Example
book = Book("Optimization", "Max Musterman")
print(book.title)

pickle_data = pickle.dumps(book)
new_book = pickle.loads(pickle_data)
print(new_book.title)

#---------------------------------------------------------------------------------
"""
References:
1- https://docs.python.org/3/library/pickle.html#pickle-state
2- https://www.geeksforgeeks.org/python/pickle-python-object-serialization/
3- https://realpython.com/python-pickle-module/
4- https://dnmtechs.com/exploring-__setstate__-and-__getstate__-in-python-3-a-simple-example/
"""