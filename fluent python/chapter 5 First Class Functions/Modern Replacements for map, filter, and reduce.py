# coding = utf-8

def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


fact = factorial

# Example 5-5. Lists of factorials produced with map and filter compared to alternatives coded as list comprehensions
print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(fact(n) for n in range(6))  # <generator object <genexpr> at 0x000001F889497938>
print(list(map(factorial, filter(lambda n: n % 2, range(6)))))  # [1, 6, 120]
print(list(map(factorial, filter(lambda n: n % 2 == 0, range(6)))))  # [1, 2, 24]
print(list(map(factorial, filter(lambda n: n % 3, range(6)))))  # [1, 2, 24, 120]
# It means that if the lambda function body caculates simplied expressions without the "==" symbol,and there is
#   no results on its right,it equals the result which is implicitly converted to Boolean from (n % t)  is True
print([factorial(n) for n in range(6) if n % 2])

# Example 5-6. Sum of integers up to 99 performed with reduce and sum

from functools import reduce
from operator import add

print(reduce(add, range(100)))
print(sum(range(100)))
