# coding = utf-8

# 检测 python初始化的时候,是否会自动执行父类的__init__() 加载?输出只有 B init ,所以不会自动执行父类__init__() 方法

class A(object):
    def __init__(self):
        print('A init')


class B(object):
    def __init__(self):
        print('B init')


b = B()
