#fibonacci numbers module

def fib(n):
    a,b=0,1
    while b<n:
        print(b ,end=' ')
        a,b=b,a+b
    print()

def fib2(n):
    result=[]
    a,b=0,1
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result


# the code below this line is the demonstation which is show that how to be a script.
if __name__ == "__main__":
    import sys

    fib(int(sys.argv[1]))
