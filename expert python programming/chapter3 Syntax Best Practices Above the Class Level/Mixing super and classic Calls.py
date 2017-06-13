# coding = utf-8

class A(object):
    def __init__(self):
        print('A')
        super(A, self).__init__()


class B(object):
    def __init__(self):
        print('B')
        super(B, self).__init__()


class C(A, B):
    def __init__(self):
        print('C')
        # A.__init__()  TypeError: __init__() missing 1 required positional argument: 'self'
        A.__init__(self)
        B.__init__(self)


print("MRO :", [x.__name__ for x in C.mro()])

C()  # 为何只有B调用了两次,C不是?教练,这不科学
