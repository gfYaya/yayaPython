# coding=utf-8

import math

print(math.pi)
print(math.cos(math.pi / 4))
print(math.log(1024, 2))  # 对数

import random

print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))  # sampling without replacement
print(random.random())  # random float
print(random.randrange(6))  # random integer from range(6)

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))  # 平均值
print(statistics.median(data))  # 中位数
print(statistics.variance(data))  # 方差
