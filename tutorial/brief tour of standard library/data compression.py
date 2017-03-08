# coding = utf-8

import zlib

s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
# CRC32 校验码值
print(zlib.crc32(s))  # CRC:循环冗余校验码
