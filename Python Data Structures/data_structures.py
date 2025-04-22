################### Arrays ###################
from conda_build.cli.main_skeleton import thisdir

names = {"Harisystems", "test", 343, True}

################### Lists in Python ###################

names = ["Hari", "test", "john", "perry", "mary"]

#print(names)
#print(names[0])
#print(names[-1])
#print(names[2:])

################### Add list Elements ###################

names.append("ahmed")    # add the new element at the end of the list
names.insert(1, "alice")    # with adding the new element at specific position

################### Remove elements of lists ###################

names.remove("test")



################### Sort lists ###################
names.sort(reverse=True)


################### Join Lists ###################
names = ["Hari", "test", "john", "perry", "mary"]
countries = ["India", "USA", "Canada", "UK", "Japan"]

result = names + countries

for i in countries:
    names.append(i)

names.extend(countries)


################### Tuples in Python ###################
# Tuples are immutable
numbers = (1, 2, 3, 4)
thisistuple = ("kiwi", "mango", "banana", "apple", "strawberry")
#print(thisistuple[-2])
#print(thisistuple[2:4])

# Update Tuples
l = list(thisistuple)
l[0] = "Berry"
t = tuple(l)
#print(l)
#print(thisistuple)
#print(t)

# Join Tuples
numbers = (1, 2, 3, 4)
tuple3 = thisistuple + numbers
#print(tuple3)


################### Dictionaries in Python ###################
# Key value
# name = Max
# email = max.mustermann@gmail.com
# phone = 879645356

customer = {
    "name" : "Max",
    "email" : "max.mustermann@gmail.com",
    "phone" : 8759584,
    "verified" : True
}

# Add Dictionary Items
customer["name"] = "Hari"  # update
customer["picode"] = "500001"  # adding

# Remove Dictionary Items
customer.pop("phone")

# Nested Dictionaries
customer1 = {
    "name" : "Max",
    "email" : "max.mustermann@gmail.com"
}
customer2 = {
    "name" : "Hari",
    "email" : "hari@gmail.com"
}
customer3 = {
    "name" : "John",
    "email" : "john@gmail.com"
}
mydic = {
    "cust1" : customer1,
    "cust2" : customer2,
    "cust3" : customer3
}

################### Sets in Python ###################
# Sets are unchangeable und
myset = {"car", "car", "bus", "auto", "cycle", "train"}

# Add Set Items
# We use the method add() to add items to particular set
myset.add("van")
myset.add(22)

# Remove Set Items with remove() method
myset.remove("car")

# Join Set Items with union() method
myset1 = {"car", "car", "bus", "auto", "cycle", "train"}
myset2 = {3, 5, 6, 7, 8}

set3 = myset1.union(myset2)
print(set3)