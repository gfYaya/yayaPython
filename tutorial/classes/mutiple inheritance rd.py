# coding = utf-8

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


# class D(B, C):
class D:
    def __init__(self, d):
        # super().__init__(d)
        b1 = B.__init__(self, d)
        c1 = C.__init__(self, d)

        print('D')
        self.d = d


'''
报错:也就意味着如果不使用class D(B,C)这种继承,无法在子类中调用他们的构造器
即:继承也需要进行声明,再调用构造器
'''

d = D('d')
d.comeon()
