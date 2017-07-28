# coding = utf-8

# Example 4-1. Encoding and decoding

# Converting from code points to bytes is encoding; converting from bytes to code points
#   is decoding. See Example 4-1.
# 个人从博客和Java中理解,encode是二进制到字符串的转换,decode相反,百度好多博客也是如此说明的
# 补充：encode和decode本意表示两个想法的字符编码转换过程,相互之间是可逆的,没有什么必然谁向另一个进行转换的过程

s = 'café'
d = s.encode('utf-8')
print(d)
b = d.decode()
print(b)
