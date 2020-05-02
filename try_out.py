import random
import builder


def shuffle(deck):
    for i in range(len(deck)-1, 0, -1):
        j = random.randint(0, i + 1)
        deck[i], deck[j] = deck[j], deck[i]
    return deck


deck = builder.buildBasicDeck()
for card in deck:
    print(card.getName())
shuffle_deck = shuffle(deck)
print("==============")
for card in shuffle_deck:
    print(card.getName())
