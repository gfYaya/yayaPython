# coding = utf-8

# Example 7-25. Module clockdeco_param.py: the parameterized clock decorator

import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):  # decorator parameter
    def decorate(func):  # function object which is decorated
        def clocked(*_args):  # function parameters are passed here
            t0 = time.time()
            _result = func(*_args)
            elapsed = time.time()
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            # print(locals()) # the current local symbol table => the function local attributes?
            print(fmt.format(**locals()))
            return _result

        return clocked

    return decorate


if __name__ == '__main__':

    @clock()
    def snooze(seconds):
        time.sleep(seconds)


    for i in range(3):
        # snooze(.123)
        snooze(3)

    print('---------------------------')


    @clock('{name}: {elapsed}s')
    def snooze_2(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze_2(.123)

    print('---------------------------')


    @clock('{name}({args}) dt={elapsed:0.3f}s')
    def snooze_3(seconds):
        time.sleep(seconds)


    for i in range(3):
        snooze_3(.123)
