# coding = utf-8

class folder(list):
    def __init__(self, name):
        self.name = name

    def dir(self):
        print("I am the %s folder. " % self.name)
        for element in self:
            print(element)


the = folder('secret')
print(the)
the.append('pics')  # the[0] ='pics'
the.append('videos')  # the[1] = 'videos'
the.dir()

# print(the[0])  # pics
print(the['name'])  # TypeError:list indices must be integers or slices, not str
# 属性调用部分不如JS 灵活
