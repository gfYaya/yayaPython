# coding = utf-8

# Example 7-17. An improved clock decorator

import functools
import time


def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = {'%s=%s' % (k, w) for k, w in sorted(kwargs.items())}
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked

# 已经证明 如果装饰器如此定义,那么必须要有 decorator()这种立即执行,装饰器函数名称后面必须要有括号,传入的第一个参数认为是
# 装饰器的参数 ,如果不加入圆括号,则传入的第一个参数 是被装饰器修饰的函数对象
# expert python grogramming下chapter2 中 decorators.py的代码
