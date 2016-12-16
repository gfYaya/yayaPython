# code segment 1
try:
    raise KeyboardInterrupt
except:
    pass
finally:
    print('Goodbye ,World')
'''  result: When an exception has occurred in the try clause and has not been handled
  by an except clause (or it has occurred in an except or else clause),
  it is re-raised after the finally clause has been executed.
'''


# code segment 2
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division zero error')
    else:
        print("result is :", result)
    finally:
        print('excuting finally clause')


divide(1, 2)
divide(1, 0)
