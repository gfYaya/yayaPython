# coding = utf-8

class FirstClass():
    def _get_price(self):
        return '$500'

    price = property(_get_price)


class SecondClass(FirstClass):
    def _get_price(self):
        return '$20'

    price_nd = property(_get_price)


plane_ticket = SecondClass()
print(plane_ticket.price)  # $500  =>python 方法完全是动态绑定?
print(SecondClass.mro())
print(plane_ticket.__dict__)  # a empty dictionary?

another_ticket = SecondClass()
print(another_ticket.price_nd)  # $20
print(another_ticket.__dict__)

'''
results : 应该是相同的方法 依据mro的顺序 后者会覆盖前者
目前测试的仅仅是 property函数
其他是否都是如此 未知
'''
