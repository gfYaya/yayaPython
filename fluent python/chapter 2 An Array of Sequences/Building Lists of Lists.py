# coding = utf-8

# Example 2-12. A list with three lists of length 3 can represent a tic-tac-toe board

board = [['_'] * 3 for i in range(3)]
print(board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
board[1][2] = 'X'
print(board)  # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]

print('----------------------')
weird_board = [['_'] * 3] * 3
print(weird_board)  # [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
weird_board[1][2] = 'X'
print(weird_board)  # [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]
# 和JS一样,引用的类型发生变化之时,生成的新容器也发生了改变,JS的五大基础类型不会触发,虽然
#   Python都是对象类型,但是number,string都是immutable的.

# a = 1
a = "1"
b = []
b.append(a)
b.append(a)
b.append(a)
print(b)
a = "2"
print(b)
