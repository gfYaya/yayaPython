# coding = utf-8

# Example 5-1. Create and test a function, then read its __doc__ and check its type

def factorial(n):
    '''returns n1'''
    '''ssss'''  # is not print in the console as the interpreter run the 'print(factorial.__doc__)' operation
    # return 1 if n < 2 else n * factorial(n - 1)  #=>1405006117752879898543142606244511569936384000000000
    return 1 if n == 1 else n * factorial(n - 1)  # =>1405006117752879898543142606244511569936384000000000
    # return 1 if 1 else n * factorial(n - 1)  # => 1
    # return 1 if True else n * factorial(n - 1) # => 1


print(factorial(42))
print(factorial.__doc__)
print(type(factorial))

# Example 5-2. Use function through a different name, and pass function as argument

"""Example 5-2 shows the “first class” nature of a function object. We can assign it a variable
fact and call it through that name. We can also pass factorial as an argument to
map. The map function returns an iterable where each item is the result of the application
of the first argument (a function) to succesive elements of the second argument (an
iterable), range(10) in this example."""

fact = factorial
print(fact)
print(fact(5))
map_a = map(factorial, range(11))
print(map_a)
# print(list(map_a)) # recursion  => RecursionError: maximum recursion depth exceeded in comparison
# print(list(map(fact,range(11)))) => RecursionError: maximum recursion depth exceeded in comparison
