# coding = utf-8

class MyClass():
    def __new__(cls, *args, **kwargs):
        print('myclass __new__ called')
        return object.__new__(cls)  # default factory

    def __init__(self):
        print('myclass __init__ called')
        self.a = 1


# instance = MyClass()

class MyOtherClassWithoutAConstructor(MyClass):
    pass


instance = MyOtherClassWithoutAConstructor()
