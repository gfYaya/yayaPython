# coding = utf-8

# Example 7-18. The very costly recursive way to compute the nth number in the Fibonacci series

tmp = __import__('How It Works')
# tmp = __import__('Implementing a Simple Decorator')
import functools


# print(tmp.clock)

@functools.lru_cache()
@tmp.clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(6))
