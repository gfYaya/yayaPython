# coding = utf-8

class BaseBase(object):
    def __init__(self, *args, **kwargs):
        print('basebase')
        super(BaseBase, self).__init__()


class Base1(BaseBase):
    def __init__(self, *args, **kwargs):
        print('base1')
        super(Base1, self).__init__()


class Base2(BaseBase):
    def __init__(self, *args, **kwargs):
        print('base2')
        super(Base2, self).__init__()


class MyClass(Base1, Base2):
    # def __init__(self): #TypeError: __init__() takes 1 positional argument but 2 were given
    def __init__(self, args):
        print("the Mro of MyClass:", MyClass.__mro__)
        print('my base')
        super(MyClass, self).__init__()
        # super(MyClass, self).__init__(args)


m = MyClass(10)
