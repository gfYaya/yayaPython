# coding = utf-8

class Mama(object):  # this is the old way
    def says(self):
        print('do your homework')


class Sister(Mama):
    def says(self):
        # the funciton is belonged to the superclass Mama.class ,but the argument is pass by itself
        Mama.says(self)
        print('and clean your bedroom')


anita = Sister()
anita.says()


# another way
class LittleSister(Mama):
    def says(self):
        # it's hard to be used as you face a mutiple inheritance schema
        super(LittleSister, self)
        print('and clean your bedroom')


anita_2 = LittleSister()
anita_2.says()
