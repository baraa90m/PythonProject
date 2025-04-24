# *kwargs (keyword arguments)

def intro(**data):
    print("Datatype Args", type(data))
    print("----------------------------")
    for key, value in data.items():
        print("{} : {}".format(key, value))

if __name__ == "__main__":
    intro(firstname="Max", lastnmae="Mustermann", age =24, cell=2323, pincode=65372)