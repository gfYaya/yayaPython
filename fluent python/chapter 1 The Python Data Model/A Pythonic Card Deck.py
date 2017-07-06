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

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print(beer_card)
