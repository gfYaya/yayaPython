# coding = utf-8

# Example 7-13. A broken higher-order function to calculate a running average without keeping all history

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        # count += 1  # UnboundLocalError: local variable 'count' referenced before assignment
        # 此时 使用count是当前作用域的变量(count = xx这种操作是直接在本作用域先创建一个变量,
        #  并优先使用该本地作用域变量) 不是上一层作用域的
        # total += new_value
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


avg = make_averager()
print(avg(10))
