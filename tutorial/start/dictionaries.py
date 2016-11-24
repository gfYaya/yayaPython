# coding=utf-8

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['guido']
tel['irv'] = 4127
print(tel)
telList = list(tel.keys())
print(telList)
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)

# show that ,if you store using a key which is already in use,the old value associate with that key is forgotten.
tel_2 = {'a': 1, 'a': 2}
print(tel_2)

r = dict([('sape', 4139), ('guido', 4172), ('jack', 4098)])
print(r)

s = {x: x ** 2 for x in (2, 4, 6)}  # dictionary comprehension
print(s)

t = dict(sape=4139, guide=4172, jack=4098)
print(t)
