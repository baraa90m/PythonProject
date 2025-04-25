# Class Program

class Greet():

    # class attribute
    course = "Python for beginners"

    def greet_user(self):
        print("Hello Developer")

# Creating a local object and Instantiating a class object
if __name__ == "__main__":
    wish = Greet()
    wish.greet_user()
    print(wish.course)
