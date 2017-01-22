#  coding =utf-8
#  python2
#  url : http://mp.weixin.qq.com/s?__biz=MzIxNjM4NDE2MA==&mid=2247484024&idx=1&sn=5843fb7555719d7085545b77be5f1397&chksm=978895b7a0ff1ca1050e09a5525fbdd7d535bced2cb0742deea8d7b39a03ab979c5b41628814&mpshare=1&scene=23&srcid=0117n2yLa14z04Ms1GglGLMC#rd

class BaseClass(object):
    def __init__(self, value):
        self.value = value
        print('Init BaseClass')
        print('Value is {0}'.format(self.value))


class TimeTwo(object):
    def __init__(self):
        self.value *= 2
        print('Init TimeTwo')
        print('Value is {0}'.format(self.value))


class PlusFive(object):
    def __init__(self):
        self.value += 5
        print('Init PlusFive')
        print('Value is {0}'.format(self.value))


class SubClass(BaseClass, TimeTwo, PlusFive):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        TimeTwo.__init__(self)
        PlusFive.__init__(self)


subclass = SubClass(1)
print(subclass.value)
