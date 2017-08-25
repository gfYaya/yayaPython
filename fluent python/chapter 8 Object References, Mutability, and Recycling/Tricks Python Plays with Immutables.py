# coding = utf-8

# Example 8-20. A tuple built from another is actually the same exact tuple

t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)  # True

t3 = t1[:]
print(t3 is t1)  # True
