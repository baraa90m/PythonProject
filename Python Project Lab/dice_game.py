# Dice Game

import random

class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


# Object Instantiating
dice = Dice()
first, second = dice.roll()
print(first, second)