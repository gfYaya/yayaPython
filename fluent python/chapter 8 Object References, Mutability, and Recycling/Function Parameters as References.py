# coding = utf-8

# Example 8-11. A function may change any mutable object it receives

def f(a, b):
    a += b
    return a


x = 1
y = 2
print(f(x, y))  # 3
print(x, y)  # 1,2

a = [1, 2]
b = [3, 4]
print(f(a, b))  # [1, 2, 3, 4]
print(a, b)  # [1, 2, 3, 4] [3, 4]

t = (10, 20)
u = (30, 40)
print(f(t, u))  # (10, 20, 30, 40)
print(t, u)  # (10, 20) (30, 40)

# result :immutable type is not changed , list is changed
