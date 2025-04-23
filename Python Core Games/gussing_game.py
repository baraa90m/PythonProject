# Gussing Game

import random

guess = 0
randNum = random.randrange(1, 11)
#randNum = 8
while guess != randNum:
    guess = int(input("Try to guess your number: "))
    if guess == randNum:
        print("Congrats! You guessed the right number!")
    if (guess > randNum):
        print("Wrong, your guessing number is high.")
    if (guess < randNum):
        print("Wrong, your guessing number is low.")