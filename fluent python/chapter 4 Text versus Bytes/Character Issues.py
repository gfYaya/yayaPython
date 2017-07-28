# coding = utf-8

# Example 4-1. Encoding and decoding

# 个人从Python博客和对Java中理解,encode是code point(OS层,非JVM层,Java JVM层是Unicode码)的转换,
#  decode相反,百度好多Python博客也是如此说明的
# 补充：encode和decode本意表示两个相反的字符编码转换过程,相互之间是可逆的,没有什么必然谁向另一个进行转换的过程

# In Python,Converting from code points to bytes is encoding; converting from bytes to code points
#  is decoding.In my opinion, this rule is contrary to Java ?
# PS :A code point is the location of a character within the code page.

s = 'café'
d = s.encode('utf-8')  # b'caf\xc3\xa9'  =>前两个是单字节的 所以不需要转换,而é 本身就是一个两个字节
# result => 存储的是unicode（对应py3的str） print的过程中会根据默认编码进行encode后写入stdout
print(d)
b = d.decode()
print(b)

s1 = '你好'
d1 = s1.encode('utf-8')
print(d1)  # b'\xe4\xbd\xa0\xe5\xa5\xbd'  => 6个字节 正好
