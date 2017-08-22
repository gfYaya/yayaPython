# coding = utf-8

# Example 8-5. t1 and t2 initially compare equal, but changing a mutable item inside tuple t1 makes it different

t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print(id(t1[-1]))
t1[-1].append(99)
print(t1)
print(id(t1[-1]))
print(t1 == t2)  # False # The identity of t1[-1] has not changed, only its value.
