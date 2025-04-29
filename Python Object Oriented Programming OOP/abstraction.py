# Abstraction

from abc import ABC, abstractmethod

class Car(ABC):
    def milage(self):
        pass

class Tesla(Car):
    def milage(self):
        print("Milage 30 kmpl")

class Honda(Car):
    def milage(self):
        print("Milage 33 kmpl")

# Object instantiate from abstract class
obj = Honda()
obj.milage()


obj_1 = Tesla()
obj_1.milage()
