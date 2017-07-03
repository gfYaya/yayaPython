# coding = utf-8

class MyClass():
    def __init__(self):
        self._my_secret_thing = 1

    def _i_get(self):
        return self._my_secret_thing

    def _i_set(self, value):
        self._my_secret_thing = value

    def _i_delete(self):
        print('neh')

    # preceding codes are used to implement descriptor protocal with the class named property?

    # class property(fget=None, fset=None, fdel=None, doc=None) => Return a property attribute.
    my_thing = property(_i_get, _i_set, _i_delete, 'the thing')


instance = MyClass()
print(instance.my_thing)
instance.my_thing = 3
print(instance.my_thing)
del instance.my_thing

help(instance.my_thing)
