matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix_2 = [[row[i] for row in matrix] for i in range(4)]
print(matrix_2)

print("row[i]:", [row[0] for row in matrix])
# matrix_3[ row[i] for i in range(4) for row in matrix ]  #Syntax Error
