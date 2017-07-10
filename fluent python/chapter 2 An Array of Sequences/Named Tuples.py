# coding = utf-8

# Example 2-9. Defining and using a named tuple type
# It shows how we could define a named tuple to hold information about a city.

from collections import namedtuple

City = namedtuple('City',
                  'name country population coordinates')  # they don’t store attributes in a per-instance __dict__.
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)  # => print(str(tokyo)) => print(repr(tokyo))

# Example 2-10. Named tuple attributes and methods (continued from the previous example)
'''
Example 2-10 shows the most useful: the _fields class attribute, the class method
_make(iterable), and the _asdict() instance method.

'''

print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
'''
_asdict() returns a collections.OrderedDict built from the named tuple
instance. That can be used to produce a nice display of city data.
'''
delhi = City._make(delhi_data)
print(delhi._asdict())
# for key, value in delhi._asdict().items():
#     print('%s : %s' % (key, value))
for tmp in delhi._asdict().items():
    print('%s : %s' % tmp)
