def make_increamentor(n):
    return lambda x: x + n  # return a function object as the JavaScript language type


f = make_increamentor(42)  # the code in this line ,the function return a function object to the variable f
print(f(2))
print(f(4))
