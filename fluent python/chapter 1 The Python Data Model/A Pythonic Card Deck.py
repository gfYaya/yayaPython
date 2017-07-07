# coding = utf-8

# Example 1-1. A deck as a sequence of cards
# it's a class to represent a deck of playing cards.

'''The collections module  implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.'''

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    # have/make/let the instance  be iterable
    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

# provides by __getitem__ method
print(deck[0], deck[-1])

from random import choice

print('random', choice(deck), choice(deck))

print(deck[0:3])
print(deck[12::13])  # 12 => 'A' ,the thirteenth char

# for card in deck:
#     print(card)

print("------------")
suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
