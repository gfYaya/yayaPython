# coding = utf-8

# Example 4-2. A five-byte sequence as bytes and as bytearray

cafe = bytes('café', encoding='utf_8')
print(cafe)
print(cafe[0])
print(cafe[:1])

cafe_arr = bytearray(cafe)
print(cafe_arr)
print(cafe_arr[0])
print(cafe_arr[-1:])

import array

numbers = array.array('h', [-2, -1, 0, 1, 2])  # 'h' => short interger
octets = bytes(numbers)
print(octets)
