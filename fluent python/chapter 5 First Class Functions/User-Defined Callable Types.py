# coding = utf-8

# Example 5-8. bingocall.py: A BingoCage does one thing: picks items from a shuffled list

import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            # Removes the item with the index i from the array and returns it.The argument defaults to -1
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self, *args, **kwargs):
        return self.pick()


bingo = BingoCage(range(3))
print(bingo.pick())
print(bingo())  # A class implementing __call__ is an easy way to create function-like objects.
#  Implementation of the () operator; a.k.a. the callable object protocol.
print(callable(bingo))  # Return whether the object is callable.
