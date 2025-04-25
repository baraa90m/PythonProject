# Function with default parameter value

def greet(name, msz="Good morning!"):
    print("Hello", name +" "+ msz)

greet("John", "How are you doing?")
greet("Peter")

print("--------------------------------------------------------")

# Function with multiple parameter values

def greet(name, age, cell, address, pincode, country):
    print(f"Hi {name} {age} {cell} {address} {pincode} {country} !")

greet("Alice", 23, 434343, "Elisabeth street", 12322, "USA")

print("--------------------------------------------------------")

# Function with return keyword

def add(a, b):
    return a + b

res = add(2, 3)
print(res)

print("--------------------------------------------------------")

