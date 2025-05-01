# Card and Deck Game
import itertools, random

# Make a deck of cards
deck = list(itertools.product(range(1, 14), ["Spade", "Heart", "Diamond", "Club"]))


# Shuffles the cards
random.shuffle(deck)
#print(deck)


# Draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])
