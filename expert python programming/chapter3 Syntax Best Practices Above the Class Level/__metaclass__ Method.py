# coding = utf-8

def method(self):  # Error  # Is the argument 'self'  urgent need?
    # def method():
    return 1


klass = type('MyClass', (object,), {'method': method})
instance = klass
# print(instance.method())
print(instance.method(1))
