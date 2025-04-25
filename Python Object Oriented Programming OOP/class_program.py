# Creating a class

class Greet():

    course = "Python for beginners"  # class attribute

    def greet_user(self):
        print("Hello Developer")

# Class Constructors: We have two types of class constructors
# 1- Default Constructors:
class Harisystems:
    def __init__(self):
        self.course = "Python for beginners"

    def access(self):
        print(self.course)


# 2- Parametrised Constructor:



# Creating a local object and Instantiating a class object
if __name__ == "__main__":
    #wish = Greet()
    #wish.greet_user()
    #print(wish.course)
    obj = Harisystems()
    obj.access()