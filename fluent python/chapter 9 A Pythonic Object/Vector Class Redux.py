# coding = utf-8

# Example 9-2. vector2d_v0.py: methods so far are all special methods

import math
from array import array


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        print(i for i in (self.x, self.y))
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r},{!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # ord: Given a string representing one Unicode character, return an integer representing
        #  the Unicode code point of that character.
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # hypot: Return the Euclidean distance, sqrt(x*x + y*y).
        return math.hypot(self.x, self.y)

    def __bool__(self):
        print('vector2d bool')
        return bool(abs(self))


# Example 9-1. Vector2d instances have several representations

v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x, y = v1
print(x, y)  # A Vector2d can be unpacked to a tuple of variables,because of iter().And the duck type?
print(v1)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
octets = bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1), bool(Vector2d(0, 0)))
