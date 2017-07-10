# coding = utf-8

# Example 2-3. The same list built by a listcomp and a map/filter composition

symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

'''Note that filter(function, iterable) is equivalent to the generator expression
(item for item in iterable if function(item))
if function is not None and (item for item in iterable if item) if function is None.
'''
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))  # the lambda expression generates a function object
print(beyond_ascii)

# The following codes are a simple speed test comparing listcomp with filter/map.
# https://github.com/fluentpython/example-code/blob/master/02-array-seq/listcomp_speed.py
import timeit

TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))


clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')
