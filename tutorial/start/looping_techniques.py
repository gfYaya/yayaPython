# coding=utf-8

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, ':', v)

for i, v in enumerate(['tic', 'tac', 'toe']):  # function enumerate() returns a list with tuples
    print(i, ',', v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# function reversed is to return a reversed sequence
for x in reversed(range(1, 10, 2)):
    print(x)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN')]
print('raw_data:', raw_data)
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
