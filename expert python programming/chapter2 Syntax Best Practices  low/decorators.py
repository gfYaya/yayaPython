# coding = utf-8

# the syntax before the decorators:
class WhatFor_1(object):
    def it(cls):
        print('work with %s' % cls)

    it = classmethod(it)

    def uncommon(self):
        print('I counld be a global function')

    uncommon = staticmethod(uncommon)


# the decorator syntax is easier and lighter understand
class WhatFor(object):
    @classmethod
    def it(cls):
        print('work with %s' % cls)

    @staticmethod
    def uncommon():
        print('I counld be a global function')


this_is = WhatFor()
this_is.it()
this_is.uncommon()


# http://www.cnblogs.com/SeasonLee/articles/1719444.html
# decorators are created with series closures ?
def salesgirl(discount):
    def expense(method):
        def server(*args):
            print('salesgirl: Hello, what do you want?', method.__name__)
            result = method(*args)
            if result:
                print('Salesgirl: This shirt is 50$, as an older user,we promised to discount '
                      'at %d%%' % discount)
            else:
                print("Salesgirl: Now how about trying another style?")
            return result

        return server

    return expense


# if __name__ == '__main__' :
@salesgirl(50)
def try_this_shirt(size):
    if size < 50:
        print('I: %d inches is too small to me' % size)
        return False
    else:
        print('I: %d inches is just enough' % size)
        return True


result = try_this_shirt(38)
print('Mum, do you want to buy this?', result)
