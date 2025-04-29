# Access Modifiers
# Public, protected and private

class Greet:
    #public data member
    var1 = None

    #protected data member
    _var2 = None

    # private data member
    __var3 = None

    #class constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    # public member function
    def accessPublicMembers(self):
        print("Public Data Members:", self.var1)

    # protected member fuction
    def _accessProtectedMembers(self):
        print("Protected Data Members:", self._var2)

    # protected member fuction
    def __accessPrivateMembers(self):
        print("Private Data Members:", self.__var3)

#child class
class Sub(Greet):
    # constructor
    def __init__(self, var1, var2, var3):
        Greet.__init__(self, var1, var2, var3)

    def ProtectedMembers(self):
        self._accessProtectedMembers()




obj = Sub("One", 2, "Three")
obj.accessPublicMembers()
obj.ProtectedMembers()


# Example:
class BankAccount:
    def __init__(self, balance = 1000):
        self.__balance = balance
    def display_balance(self):
        return self.__balance
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            print("Successfully withdrawn ", amount)


account = BankAccount()
account.withdraw(20)
account.display_balance()
