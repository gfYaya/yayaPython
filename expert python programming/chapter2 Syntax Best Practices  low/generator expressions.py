# coding = utf-8

# list comprehensions is created with brackets,
# generation expressions is used parenthese to replace 'yield' operation

# These kinds of expressions are called generator expressions or genexp.
iter = (x ** 2 for x in range(10) if x % 2 == 0)
for el in iter:
    print(el)

print(iter)  # <generator object <genexpr> at 0x000001F9B4C17990>
