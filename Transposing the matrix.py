'''Transposing the matrix'''
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n=len(matrix1)
transposed=[]
for _ in range(n):
    transposed.append([0]*n)
for i in range(n):
    for j in range(n):
        transposed[j][i]=matrix1[i][j]
for i in transposed:
    print(i)
# print(transposed)