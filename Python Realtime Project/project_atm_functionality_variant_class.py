# Project ATM Functionality
# A2Z Bank by Harisystems

import time    # this time command so I can make the code wait before doing something
import sys     # this imports system command
from datetime import datetime

class BankAccount:

    def __init__(self, balance = 100):
        self.balance = balance
        self.transactions = []

    def display_balance(self):
        print(f"Current Balance: {self.balance}$")

    def add_transaction(self, action, amount):
        if len(self.transactions) >= 10:
            self.transactions.pop(0)
            self.transactions.append((action, amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount % 10 != 0:
            print("Amount must be a multiple of 10.")
        else :
            self.balance -= amount
            print(f"Successfully withdrew {amount}$, new balance: {self.balance}$")
            self.transactions.append((datetime.today().strftime("%Y.%m.%d %H:%M:%S"), "Withdrew", amount))

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.balance += amount
            print(f"Successfully deposited {amount}$, new balance: {self.balance}$")
            self.transactions.append((datetime.today().strftime("%Y.%m.%d %H:%M:%S"), "Deposited", amount))

    def show_transactions(self):
        print(f"Last transactions:")
        for date_time, action, amount in self.transactions:
            print(f"{date_time} : ({action} : {amount}$)")

def main():
    account = BankAccount()
    print("""
    Password is 1212.
    Don't use caps.
    You can only see your previous 10 transactions.""")
    time.sleep(1)

    for attempt in range(3):
        pin = int(input("Please enter PIN: "))
        if pin == 1212:
            print("Correct PIN")
            break
        else:
            print("Incorrect PIN")
            time.sleep(1)
    else:
        print("Wait 2 minutes to try again.")
        time.sleep(60)
        sys.exit()
    while True:
        time.sleep(0.75)
        menu = input("""Please select an option:
        1- Display Balance
        2- Withdraw Funds
        3- Deposit Funds
        4- Show Transactions
        5- Return Card
        --->: """)
        if menu == "1":
            account.display_balance()
        elif menu == "2":
            try:
                amount = int(input("Enter amount to withdraw (multiple of 10):"))
                account.withdraw(amount)
            except ValueError:
                print("Invalid Input.")
        elif menu == "3":
            try:
                amount = int(input("Enter amount to deposit:"))
                account.deposit(amount)
            except ValueError:
                print("Invalid Input.")
        elif menu == "4":
            account.show_transactions()
        elif menu == "5":
            print("Thank you for banking.")
            sys.exit()
        else:
            print("Please select a valid option.")


if __name__ == "__main__":
    main()