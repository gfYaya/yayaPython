# coding = utf-8

# Example 2-20. Creating, saving, and loading a large array of floats

# It shows creating, saving, and loading an array of 10 million floating-point random numbers.

from array import array
from random import random

# array(typecode [, initializer]) -> array  , the typecode is C type
floats = array('d', (random() for i in range(10 ** 7)))
print(floats[-1])

fp = open('floats.bin', 'wb')  # w ->open for writing, truncating the file first , b ->binary mode
# Write all items (as machine values) to the file object fp.
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')  # open for reading (default)
# Read 10**7 items (as machine values) from the file object fp and append them to the end of the array.
floats2.fromfile(fp, 10 ** 7)
fp.close()
print(floats == floats2)
print(floats2[-1])
