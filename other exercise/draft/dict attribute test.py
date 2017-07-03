# coding = utf-8

#  verify the __dict__ whether includes the attribute of an instance ,or both of the
# instance and class's attribute
class Test():
    a = 's'

    def __init__(self, b):
        self.b = b


if __name__ == '__main__':
    t = Test('b')
    print("instance:", t.__dict__)  # without the class attribute ,only instance attribute
    print("class", Test.__dict__)  # without the instance attribute
