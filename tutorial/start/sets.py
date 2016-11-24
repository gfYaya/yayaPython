basket = {'apple', 'orange', 'banana', 'orange', 'pear',
          'apple'}  # we create a set with a pair of cirly braces or a set() function
print(basket)  # show that the sets eleminate the duplicate elements as you create sets
t = {}
print(t)  # we can't create an mepty set with {} ? but the console have shown that
print('apple' in basket)
print('crabgrass' in basket)
a = set('abracadabra')
b = set('alacazam')

print('a:', a)
print('b:', b)
print('a-b:', a - b)
# print('a+b:', a+b)    # TypeError,unsupported operand types for +:'set' and 'set'
print('a|b:', a | b)
print('a&b:', a & b)
print('a^b:', a ^ b)

# show that the function set() make the data structure which is iterable  changed to a set
c = set(['1', '2', '3'])
print('c:', c)
d = set(range(4))
print('d:', d)

a_1 = {x for x in 'abracadabra' if x not in 'abc'}
print(a_1)
