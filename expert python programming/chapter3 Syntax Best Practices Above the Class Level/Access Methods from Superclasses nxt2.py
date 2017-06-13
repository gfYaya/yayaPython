# coding = utf-8

class BaseBase(object):
    def method(self):
        print('BaseBase')


class Base1(BaseBase):
    pass


class Base2(BaseBase):
    def method(self):
        print('Base2')


class MyClass(Base1, Base2):
    pass


here = MyClass()
here.method()  # Base2


def L(klass):
    # The __mro__ attribute of a class (which is read-only) stores the result of
    #   the linearization computation, which is done when the class definition is loaded.
    # return [k.__name__ for k in klass.__mro__]
    return [k.__name__ for k in klass.mro()]  # the value object.mro() returns equals object.__mro__


print(L(MyClass))  # ['MyClass', 'Base1', 'Base2', 'BaseBase', 'object']
