"""
What is Abstract Base Class?
* Abstract Base Classes (ABCs) in python serve as a powerful tool.
* They are used to enforce structure and consistency in object-oriented-programs.
* ABCs help in defining common interfaces for classes.
* They ensure the presence of specific methods that must be implemented by subclasses.
The use of ABCs contributes to making code more organized and maintainable.
"""

from abc import ABC, abstractmethod

class Fruit(ABC):

    @abstractmethod
    def have_seed(self):
        pass

    @abstractmethod
    def color(self):
        pass

class Apple(Fruit):
    def __init__(self):
        self.seed = True
        self.color = 'Red'
    def have_seed(self):
        return self.seed
    def color(self):
        return self.color

apple = Apple()
print(apple.have_seed())
print(apple.color)



# Hint: by creating an ABC class for example class Fruit, we enforce that every
# subclass must have certain methods like have_seed or have_color