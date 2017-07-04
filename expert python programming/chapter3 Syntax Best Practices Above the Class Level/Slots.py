# coding = utf-8

class Frozen(object):
    __slots__ = ['ice', 'cream']
    t = 's'


print(dir(Frozen))  # 's','ice','cream' ,they are all included in dir() sequence,does '__slots__' take effect?

print('__dict__' in dir(Frozen))
print('ice' in dir(Frozen))

# python 声明变量的时候需要同时进行赋值,如同java的局部变量,slots声明这些变量的时候未进行实例化,所以需要使用前先赋值
#  而且slots是用来限制一个实例对象可以拥有那些属性 而不是用来添加属性的 ,但是从glagla.t来看凡是也总有例外
glagla = Frozen()
glagla.ice = 1
print(glagla.ice)
glagla.cream = 1
# glagla.icy = 1  # Error
print(glagla.t)
