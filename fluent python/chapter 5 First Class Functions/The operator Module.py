# coding = utf-8

# Example 5-21. Factorial implemented with reduce and an anonymous function

from functools import reduce


def fact(n: int) -> 'factorial':
    return reduce(lambda a, b: a * b, range(1, n + 1))


print(fact(5))

# Example 5-22. Factorial implemented with reduce and operator.mul

from operator import mul


def fact(n):
    return reduce(mul, range(1, n + 1))


print(fact(5))

# Example 5-23. Demo of itemgetter to sort a list of tuples (data from Example 2-8)

metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
              ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
              ]

"""
        Return a callable object that fetches the given item(s) from its operand.
    After f = itemgetter(2), the call f(r) returns r[2].
    After g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
"""
from operator import itemgetter

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

cc_name = itemgetter(1, 0)
for city in metro_data:
    # If you pass multiple index arguments to itemgetter, the function it builds will return
    # tuples with the extracted values:
    print(cc_name(city))

# Example 5-24. Demo of attrgetter to process a previously defined list of namedtuple
#   called metro_data (the same list that appears in Example 5-23)

from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metor_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) for name, cc, pop, (lat, long) in metro_data]
print(metor_areas[0])
print(metor_areas[0].coord.lat)

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metor_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))  # Use the attrgetter defined in to show L63 only city name and latitude.

import operator

print([name for name in dir(operator) if not name.startswith('_')])

# Example 5-25. Demo of methodcaller: second test shows the binding of extra arguments

from operator import methodcaller

s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s))
hibernate = methodcaller('replace', ' ', '-')
print(hibernate(s))
