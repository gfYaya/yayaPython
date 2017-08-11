# coding = utf-8

# Example 5-26. Using partial to use a two-argument function where a one-argument callable is required

from functools import partial
from operator import mul

triple = partial(mul, 3)
print(triple(7))
print(list(map(triple, range(1, 10))))

# Example 5-27. Building a convenient Unicode normalizing function with partial

import unicodedata, functools

nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))


# Example 5-28. Demo of partial applied to the function tag from Example 5-10

def tag(name, *content, cls=None, **attrs):
    """Generates on or more HTML Tag"""
    if cls is not None:
        attrs['class'] = cls

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''

    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


picture = functools.partial(tag, 'img', cls='pic-frame')
print(picture(src='wumpus.jpeg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)
