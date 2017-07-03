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
