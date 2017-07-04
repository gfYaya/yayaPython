# coding = utf-8


'''书上那个代码 有点问题
我在仿的时候就觉得不对劲 果然我的感觉是对的
要么就是python3 自己修改了
因为 我觉得这么设计很鸡肋
灵活性太低了
必须有self这个参数的话 那么 这个函数只能用来给type方式绑定对象了
而python又不支持重载
所以 完全是当作两个函数使用了
所以 我觉得 书上这么写有问题
'''

def method(self):  # Error  # Is the argument 'self'  urgent need?
    # def method():
    return 1


klass = type('MyClass', (object,), {'method': method})
instance = klass
# print(instance.method())
print(instance.method(1))
