# coding=utf-8

# 测试fibo函数的keyword arguments 是否会产生缓存
# https://zhuanlan.zhihu.com/p/26151166
# 补证: http://python.jobbole.com/86100/

def fibo(n, cache=None):
    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]
    if n == 0 or n == 1:
        return 1
    else:
        cache[n] = fibo(n - 2, cache) + fibo(n - 1, cache)

    print(cache)
    return cache[n]


fibo(10)  # cache保留下来了,但是 貌似意义不大,与后续的行为不一致,因为这个列表没有最终保留下来
fibo(9)  # 证明了 表没有最终保留下来 keyword arguments使用None 取消"永久"缓存可行


# keyword arguments test
def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1)  # list1 = [10, 'a']
print("list2 = %s" % list2)  # list2 = [123]
print("list3 = %s" % list3)  # list3 = [10, 'a']

print('\n')


# keyword arguments test nd
def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1)  # list1 = [10]
print("list2 = %s" % list2)  # list2 = [123]
print("list3 = %s" % list3)  # list3 = ['a']
