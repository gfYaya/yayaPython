# function defined outside the class
def f1(self, x, y):
    return min(x, x + y)


class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

c = C()
print(c.f(1, 2))
print(c.h())
print(c.h)
