r1 = list(range(3, 6))
print(r1)

# we write the function call with  the *-operator to unpack the arguments out of a list or tuple
args = [3, 6]
r2 = list(range(*args))
print(r2)


def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


# the dictionary can deliver keyword arguments with the **-operator
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# print(**d)
parrot(**d)
