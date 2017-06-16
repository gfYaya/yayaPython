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

print('MyClass : ', MyClass.__dict__)
print('instance -- t : ', t.__dict__)
t.new_att = 1
print(t.__dict__)
t.new_att = 'yaya'
print('t.new_att : ', t.new_att)
print('t.__dict__ : ', t.__dict__)
t.new_att = UpperString()
t.new_att = 'yaya'
print('t.new_att : ', t.new_att)  # yaya , the string literal is still lowercase
print('t.__dict__ : ', t.__dict__)
MyClass.new_att = UpperString()
t.new_att = 'yaya'
print('the third test ')  # YAYA , it's uppercase now
print('t.new_att : ', t.new_att)
print('t.__dict__ : ', t.__dict__)
