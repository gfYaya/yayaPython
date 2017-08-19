# coding = utf-8

# Example 7-15. A simple decorator to output the running time of functions

import time


def clock(func):
    print('decorated clock starts to load')

    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapse = time.perf_counter() - t0
        name = func.__name__
        # arg_str = ', '.join(repr(arg) for arg in args)
        arg_str = ', '.join(str(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapse, name, arg_str, result))
        return result

    return clocked


# Example 7-16. Using the clock decorator

# clockdeco_demo.py

@clock
def snooze(seconds: float) -> None:
    time.sleep(seconds)


@clock
def factorial(n: int):
    return 1 if n < 2 else n * factorial(n - 1)


'''
@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

Actually does this:

def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

factorial = clock(factorial)

'''


if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling facorial(6)')
    print('6! = ', factorial(6))

    print(factorial.__name__)  # clocked
