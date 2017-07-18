# coding = utf-8

# Example 2-23. Working with a deque

# warning:限制长度的时候,左边加入会挤掉右面的,右面加入同理

from collections import deque

# Returns a new deque object initialized left-to-right (using append())
# with data from iterable. If iterable is not specified, the new deque is empty.
dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-1)
print(dq)
dq.append([11, 22, 33])
print(dq)  # deque([1, 2, 3, 4, 5, 6, 7, 8, 9, [11, 22, 33]], maxlen=10) ? It's different from the book.
dq.appendleft([10, 20, 30, 40])
print(dq)
