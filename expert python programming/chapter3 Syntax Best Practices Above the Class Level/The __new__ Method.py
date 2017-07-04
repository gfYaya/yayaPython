# coding = utf-8

class MyClass():
    '''__new__ is the answer to the need for implicit initialization of
object states. It will let you define an initialization at a lower level than
__init__, which is always called.'''
    def __new__(cls, *args, **kwargs):
        print('myclass __new__ called')
        return object.__new__(cls)  # default factory

    def __init__(self):
        print('myclass __init__ called')
        self.a = 1


instance = MyClass()  # the __new__ method is auto excute before __init__?
print('---------------------')

class MyOtherClassWithoutAConstructor(MyClass):
    pass


instance = MyOtherClassWithoutAConstructor()  # 自己没有声明init 和 new方法,则直接调用父类的


class MyOtherClass(MyClass):
    def __init__(self):
        print('MyOhter class __init__ called')
        super(MyOtherClass, self).__init__()
        self.b = 2


print('------------------')
instance = MyOtherClass()  # it means that __new__ is called ealier automatically than __init__ method ?
