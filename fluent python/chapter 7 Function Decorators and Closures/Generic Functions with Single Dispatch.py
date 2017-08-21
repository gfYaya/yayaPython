# coding= utf-8

# Example 7-20. htmlize generates HTML tailored to different object types

import html


def htmlize_1(obj: object) -> str:
    content = html.escape(repr(obj))
    print('obj : %a' % repr(obj))
    return '<pre>{}</pre>'.format(content)


print(htmlize_1({1, 2, 3}))
print(htmlize_1(abs))
print(htmlize_1('Heimlich & Co.\n- a game'))
print(htmlize_1(42))
print(htmlize_1(['alpha', 66, {3, 2, 1}]))

# Example 7-21. singledispatch creates a custom htmlize.register to bundle several functions into a generic function
#   Python doesn't provide us with function or method overloading.If we make the function to be a dispatch
# function which is with a chain of if/elif (elipsis) is too huge and not extensible.

from functools import singledispatch
from collections import abc
import numbers


@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


#   Wtf?What's the difference between singledispath decoration(generic function) with the dispatch
# function or function overlaoding?In my opinion it's also tedious,even a little more complicated.

@htmlize.register(str)  # Each specialized function is decorated with @«base_function».register(«type»).
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{}</p>'.format(content)


@htmlize.register(numbers.Integral)  # numbers.Integral is a virtual superclass of int.
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


print(htmlize({1, 2, 3}))
print(htmlize(abs))
print(htmlize('Heimlich & Co.\n- a game'))
print(htmlize(42))
print(htmlize(['alpha', 66, {3, 2, 1}]))
