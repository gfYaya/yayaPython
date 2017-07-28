# coding = utf-8

# Example 4-1. Encoding and decoding

# 个人从博客和Java中理解,encode是code point(OS层,非JVM层,Java JVM层是Unicode码)的转换,decode相反,百度好多博客也是如此说明的
# 补充：encode和decode本意表示两个想法的字符编码转换过程,相互之间是可逆的,没有什么必然谁向另一个进行转换的过程

# In Python,Converting from code points to bytes is encoding; converting from bytes to code points
#  is decoding.In my opinion, this rule is contrary to Java ?
# PS :A code point is the location of a character within the code page.

s = 'café'
d = s.encode('utf-8')
print(d)
b = d.decode()
print(b)
