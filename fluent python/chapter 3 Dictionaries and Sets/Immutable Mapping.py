# coding = utf-8

# the instance of MappingProxyType is a read_only ,dynamic view of the original mapping.

# Example 3-9. MappingProxyType builds a read-only mappingproxy instance from a dict.

from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
# d_proxy[2] = 'X' # TypeError: 'mappingproxy' object does not support item assignment
d[2] = 'B'

# 说明此处是Python引用类型 同第二章的 Building Lists Of Lists中的demo一样.Python和JS存储的都是引用
print(d_proxy[2])  # B  => d_proxy is dynamic: any change in d is reflected
