def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# parrot(voltage=5.0, 'dead')
parrot('100', state='s')
parrot('a million', 'bereft of life', 'jump')


def function(a):
    pass


function(a=0)


# function(0,a=0)  => function() got multiple values for argument 'a'

def cheeseshop(kind, *arguments, **keywords):
    ''' argument :keywords,it's a dictionoary,and the keys is re-sorted '''
    print('-- Do you have any ', kind, "?")
    print("-- I'm sorry,we are all out of ", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
