# coding = utf-8

# Example 2-22. Basic operations with rows and columns in a numpy.ndarray
# It shows some basic operations with two-dimensional arrays in NumPy.

import numpy

a = numpy.arange(12)  # 1 * 12
print(a)
print(type(a))
print(a.shape)
a.shape = 3, 4  # 3 * 4 ,two dimension
print(a)

print(a[:, 1])  # a[each, 1] , get column at index 1.
print(a[..., 1])  # is equal to  a[:, 1] with the Ellipses Syntax
