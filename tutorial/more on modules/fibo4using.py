import fibo

# from fibo import fib,fib2  #error?why?
print(fibo.fib(1000) )
print(fibo.fib2(100) )
print(fibo.__name__)

myfib=fibo.fib
print(myfib(10))
myfib_2=fibo.fib2
print(myfib_2(20) )