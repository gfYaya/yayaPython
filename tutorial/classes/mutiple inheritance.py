class A:
    def __init__(self, a):
        print('A')
        self.a = a

    def comeon(self):
        print('A.comeon')


class B(A):
    def __init__(self, b):
        super().__init__(b)
        print('B')
        self.b = b

    def comeon(self):
        print('B.comeon')


class C(A):
    def __init__(self, c):
        super().__init__(c)
        print('C')
        self.c = c

    def comeon(self):
        print('C.comeon')


class D(B, C):
    def __init__(self, d):
        super().__init__()
        print('D')
        self.d = d


d = D('d')
d.comeon(d)
