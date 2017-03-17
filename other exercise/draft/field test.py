#  coding=utf-8

count = 10


def outer():
    # global count
    print(count)
    count = 100
    print(count)


outer()
