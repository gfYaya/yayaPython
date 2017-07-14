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

# a = 1
a = "1"
b = []
b.append(a)
b.append(a)
b.append(a)
print(b)
a = "2"
print(b)
