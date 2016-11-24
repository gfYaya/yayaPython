# coding=utf-8

t = 12345, 654321, 'hello!'
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)  # a nested tuple

# t[0]=88888
'''
 here is a syntax error,because the tuple is immutable,
 so that every element of tuple can't be changed.
'''

v = ([1, 2, 3], [4, 5, 6])  # there are two tuples nested in a list
print(v)

empty = ()  # an empty tuple ,and its length is zero
singleton = 'hello',
print(len(empty))
print(singleton)
print(len(singleton))
