# coding = utf-8

# Example 1-2. A simple two-dimensional vector class
''' It is a Vector class implementing the operations just described, through the
use of the special methods __repr__, __abs__, __add__ and __mul__. '''

from math import hypot  # Return the Euclidean distance, sqrt(x*x + y*y).


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # improve by Yaya
    def __mul__(self, scalar):
        if type(scalar) == int:
            return Vector(self.x * scalar, self.y * scalar)
        elif type(scalar) == Vector:
            return Vector(self.x * scalar.x + self.y * scalar.y, self.y * scalar.x + self.x * scalar.y)


a = Vector(3, 4)
b = Vector(6, 8)

print('add', a + b)  # invoke __add__ method by interpreter
print('mul_1', a * 2)  # invoke __mul__ method
print('mul_2', a * b)  # invoke __mul__ method
