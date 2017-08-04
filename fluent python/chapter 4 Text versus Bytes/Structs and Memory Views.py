# coding = utf-8

# Example 4-4. Using memoryview and struct to inspect a GIF image header
# It shows the use of memoryview and struct together to extract the width and height of a GIF image.

import struct

fmt = '<3s3sHH'  #
with open('totoro.gif', 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))

print(struct.unpack(fmt, header))

del header  # Delete references to release the memory associated with the memoryview instances.
del img
