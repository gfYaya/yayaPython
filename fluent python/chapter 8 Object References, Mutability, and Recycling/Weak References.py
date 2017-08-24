# coding = utf-8

# Example 8-17. A weak reference is a callable that returns the referenced object or None if the referent is no more

import sys
import weakref

a_set = {1, 2}
# wref = weakref.ref(a_set)
print('count sum:', sys.getrefcount(a_set))  # 2 => 当使用某个引用作为参数，传递给getrefcount()时，参数实际上创建了一个临时的引用
wref = weakref.ref(a_set, lambda _: print('obj is collected'))
print('count sum:', sys.getrefcount(a_set))  # still 2
# print('weak refer list:',weakref.getweakrefs(a_set))
print(wref)
print(wref())
a_set = {2, 3, 4}
# CPython执行该文件和 用IPython控制台打印的后续结果不一样.
print(wref())
print(wref() is None)
print(wref() is None)
print(wref)  # dead
