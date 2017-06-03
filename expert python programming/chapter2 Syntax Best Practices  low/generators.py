# coding = utf-8

def fibonacci():
    a, b=0, 1
    while True:
        yield b
        a ,b = b, b + a

fib = fibonacci()
# python 2.x
# print(fib.next())
# print(fib.next())
# print([fib.next() for i in range(10)])  # =>如果是python 2.x ,改成xrange(10)更合适

# python 3.x
print(next(fib))
print(next(fib))
print(next(fib))
print([next(fib) for i in range(10)])

# exercise by myself
for i in ( x*x  for x in range(10) ):
    # this is a generator, so is the function range() in python 3.x? or an iterator?
    print(i)