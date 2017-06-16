# coding = utf-8

class UpperString(object):
    def __init__(self):
        self._value = ''

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self._value = value.upper()


class MyClass(object):
    attribute = UpperString()


t = MyClass()
t.attribute = 'my value'
print(t.attribute)  # MY VALUE
