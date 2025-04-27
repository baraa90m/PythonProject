# Inheritance in Python


# Parent class
class Animal:
    def walk(self):
        print("walk")

# Child class
class Dog(Animal):
    def bark(self):
        print("Bark")

# Child class
class Cat(Animal):
    def sleep(self):
        print("Sleep")

# object instantiation
obj = Dog()
obj.walk()
obj.bark()

obj_cat = Cat()
obj_cat.walk()
obj_cat.sleep()