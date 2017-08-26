# coding = utf-8

# Example 8-20. A tuple built from another is actually the same exact tuple

t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)  # True

t3 = t1[:]
print(t3 is t1)  # True

# Example 8-21. String literals may create shared objects
t1 = (1, 2, 3)
t3 = (1, 2, 3)
print(t3 is t1)  # False
s1 = 'ABC'
s2 = 'ABC'
print(s2 is s1)  # True
