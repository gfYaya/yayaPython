# coding = utf-8

class FirstClass(object):
    def _get_price(self):
        return '$500'

    price = property(_get_price)


class SecondClass(FirstClass):
    def _get_price(self):
        return '$20'


plane_ticket = SecondClass()
print(plane_ticket.price)  # I expect the result print $20, but the result is $500
