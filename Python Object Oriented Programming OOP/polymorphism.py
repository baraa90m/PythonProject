# Polymorphism in Python

class Bulbul:
    def fly (self):
        print("Bulbul can fly")
    def swim(self):
        print("Bulbul can't swim")

class Ostriches:
    def fly(self):
        print("Ostriches can't fly")
    def swim(self):
        print("Ostriches can swim")

# Common interface
def flying(bird):
    bird.fly()
    bird.swim()



# Instantiation on abject
obj = Bulbul()
obj1 = Ostriches()


# Passing the object values
flying(obj)
flying(obj1)

