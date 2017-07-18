# coding = utf -8

# Example 2-21. Changing the value of an array item by poking one of its bytes
# It's an example of changing a single byte of an array of 16-bit integers.

from array import array

# numbers = array.array('h', [-2, -1, 0, 1, 1])  # I think it's a fault which the author write here
numbers = array('h', [-2, -1, 0, 1, 1])  # short signed integers (typecode 'h')
memv = memoryview(numbers)
print(len(memv))  # 貌似 __xxx__ 这种dunder方法 function_name(arg) 这种调用方式会有返回值 ,arg.function_name()返回的都是None
print(memv[0])
memv_oct = memv.cast('B')  # unsigned char
print(memv_oct.tolist())  # [254, 255, 255, 255, 0, 0, 1, 0, 1, 0]
memv_oct[5] = 4
print(numbers)
