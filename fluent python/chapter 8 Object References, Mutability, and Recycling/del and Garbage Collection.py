# coding = utf-8

# Example 8-16. Watching the end of an object when no more references point to it

import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Gone with the wind...')


ender = weakref.finalize(s1, bye)
print(ender.alive)

del s1
print(ender.alive)

s2 = 'spam'  # Gone with the wind...
print(ender.alive)  # False
