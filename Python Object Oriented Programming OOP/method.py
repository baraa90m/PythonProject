# Method in Python

class Greet:
    def greet_user(self, f_name, l_name, age):
        print(f"Hello {f_name} {l_name}, your age is {age}!")
        print(f"Welcome in our Academy!")


obj = Greet()
obj.greet_user("Max", "Mustermann", 23)