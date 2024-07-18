import numpy
mat1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 
mat2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for i,j in zip(mat1,mat2):
    # print(i,j)
    for _i,_j in zip(i,j):
        # print(_i,_j)
        x= _i + _j
        print(list(x),end=" ")
    print(end="\n")

print(numpy.add(mat1,mat2))


# mat3=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# for i in range(len(mat1)):
#     for j in range(len(mat1[0])):
#         mat3[i][j]=mat1[i][j]+mat2[i][j]
# print(mat3)