# coding = utf-8

# Example 7-4. Function reading a local and a global variable

def f1(a):
    print(a)
    print(b)


b = 6
f1(3)

# Example 7-5. Variable b is local, because it is assigned a value in the body of the function

b = 6


def f2(a):
    global b  # afterthought
    # 也意味着 Python 创建变量的时候即声明了一个当前作用域的变量,当前作用域下没
    #   有关键字修饰的变量,表示的都是local作用域,而不是nonlocal或者global 设置sys的作用域
    print(a)
    print(b)
    b = 9


f2(3)
