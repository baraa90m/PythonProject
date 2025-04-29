# Encapsulation

# Using the concept of encapsulation, we can restrict access methods and variables
# from unauthorized and hiding the data

class Lappy:
    def __init__(self):
        self.__maxprice = 2500

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, new_price):
        self.__maxprice = new_price

obj = Lappy()
obj.sell()

# Change the price
obj.setMaxPrice(4000)
obj.__maxprice = 5000   # The price will be NOT changed directly.
obj.sell()

# Conclusion: When we want to change the "maxprice", we can do it only with the method setMaxPrice().
# This means that we can't change the price directly with "obj.__maxprice = 4000"
