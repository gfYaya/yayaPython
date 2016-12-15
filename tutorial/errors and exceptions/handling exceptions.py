# code segment 1
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print("x=", x)
    print("u=", y)


# code segment 2
def this_fails():
    x = 1 / 0

try:
    this_fails()
except ZeroDivisionError as zd_err:
    print(zd_err.args)
    print("Handling run-time error", zd_err)


