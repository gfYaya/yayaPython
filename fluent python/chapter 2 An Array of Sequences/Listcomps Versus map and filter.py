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
