# coding = utf-8

#  a contextlib for with operating
class Context(object):
    def __enter__(self):
        print('entering the zone')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('leaving the zone')
        if exc_type is None:
            print('with no error')
        else:
            print('with an error %s' % exc_val)


if __name__ == '__main__':
    with Context():
        print('i am the zone')

    print('--------------the 2nd test start-------------------')
    with Context():
        print('i am the buggy one')
        raise TypeError('i ma the bug')
