# coding = utf-8

# Example 8-18. Cheese has a kind attribute and a standard representation

class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'cheese(%r)' % self.kind


# Example 8-19. Customer: “Have you in fact got any cheese here at all?”

import weakref

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))
