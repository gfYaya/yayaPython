# coding=utf-8
for element in [1, 2, 3]:
    print('iter4list', element)

for element in (1, 2, 3):
    print('iter4tuple', element)

for key in {"one": 1, "two": 2}:
    print('iter4dict', key)

for char in "123":
    print('iter4string', char)

# for line in open("D:\\ftpdown\\pm250\\city_pm250_datail_20170116-0-50.txt", 'tr'): #错误信息显示的是异步展示
#for line in open("D:\\ftpdown\\pm250\\city_pm250_datail_20170116-0-50.txt", 'tr', encoding='utf-8'):
   #print(line, end="")

s = "abc"
it = iter(s)
try:
    print(it.__next__())
    print(next(it))
    print(next(it))
    print(it.__next__())
except StopIteration:
    print("iter is over")


# an iterator of py created by myself with the demonstration
class Reverse:
    """Iterator for looping over a sequence backwards"""
    def __init__(self,data):
        self.data=data
        self.index =len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index ==0:
            raise StopIteration
        self.index =self.index - 1
        return self.data[self.index]

rev =Reverse('spam');
print( iter(rev) )
for char in rev:
    print(char)