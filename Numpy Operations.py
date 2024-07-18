import numpy as np
# 1.numpy(Attribute)
# a=(np.random.randint(low=0,high=25,size=(2,5)))#Output:-(Creates a Matrix within the range of 0,25 and in 2 rows & 3 Cols)
# print(a)
# print(np.ndim(a))#Output:-(It Gives no. of Dimensions)
# print(np.shape(a))#Output:-(It Gives no. of Rows and Cols)
# print(np.size(a))#Output:-(It Gives no. of Elements in Matrix)

# 2.numpy(Datatypes)
# (bool),(int8.int16,int32,int64),(uint8,uint16,uint32,uint64),(float16,float32,float64),(complex,complex64,complex128)
# a=np.zeros(5)#Output:-float64
# print(a.dtype)
# b=np.zeros(6)#Output:-float64
# print(b.dtype)
# c=np.zeros(6,dtype=np.int8)
# print(c.dtype)#Output:-int8
# d=np.float_(12)#Output=float64
# print(d.dtype)
# e=np.array([1,2,3],dtype="f")
# print(e)

# # To change the datatype
# '''Previously the value of a is float64 in lineNo_11'''
# a=a.astype(int)
# print(a.dtype)

# Indexing Operations using Numpy
# a=np.random.randint(low=0,high=7,size=(2,3))
# print(a)
# print(a[1][2])
# print(1)#Output:-Gives 1st row as Output
# print("----------------------------------------------------------------------------------------")
# a=np.random.randint(low=0,high=7,size=(2,3,4))
# # print(a)
# print(a[0][1][2])
# print(1)#Output:-Gives 1st row as Output
# Output:-
'''[[[6 1 0 5]
  [3 6 2 4]
  [3 5 6 3]]

 [[0 6 2 1]
  [0 4 0 2]
  [5 2 1 3]]]'''

# __________________________________________________________Slicing Operation using Numpy________________________________________________
# _________________________________________________________________________________________________________________________________________
#  ---------------------------------------------------------||||One Dimensional Array||||-------------------------------------------
# a=np.array([1,2,3,5])
# print(a[0:3])

# ------------------------------------------||||Two Dimensional Array||||----------------------------------------------------------------
# a=np.random.randint(low=0,high=15,size=(3,2))
# print(a)
# '''
# [[14 14]
#  [ 1  3]
#  [ 0 13]]'''
# print(a[1:,1:])#Output=[[3]
#                       [13]]

# a=np.random.randint(low=0,high=15,size=(3,4))
# print(a)
# '''
# [[ 7 11  1  5]
#  [ 3  7  6 13]
#  [ 3 10  6  6]]
# '''
# print(a[1:,1:])
# #  Output:-
# # [[ 7  6 13]
# #  [10  6  6]]
# print(a[::,::2])
# # Output:-
# # [[7,1]
# #  [3,6]
# #  [3,6]]


# --------------------------------------------||||Three Dimensional Array||||---------------------------------------------------
# a=np.random.randint(low=0,high=15,size=(2,3,4))
# print(a)
# Output:
# [[[10  3  6  1]
#   [ 0  0 11  3]
#   [ 9 11  0  0]]

#  [[12  7 14  1]
#   [10  7 12 13]
#   [ 8  8 14 14]]]
# print(a[:,:,0:1])
# Output:-
# [[[10]
#   [ 0]
#   [ 9]]

#  [[12]
#   [10]
#   [ 8]]]
# EXAMPLE:2
# a=np.random.randint(low=0,high=15,size=(2,3,4))
# Output:-
# [[[ 6  2 14  4]
#   [ 2 12 14  1]
#   [ 3  2 13  9]]

#  [[ 0  2  3  6]
#   [ 2  6  4 10]
#   [ 9  1  7  3]]]
# print(a)
# print(a[:,1:,::2])
# [[[ 2 14]
#   [ 3 13]]

#  [[ 2  4]
#   [ 9  7]]]

# ______________________________________________Advanced Indexing_________________________________________________________
# a=np.arange(2,15)#Output=[ 2  3  4  5  6  7  8  9 10 11 12 13 14]
# index=np.array([3,8,9])
# print(a)
# print(a[index])#Output:=[ 5 10 11]

# ----------------------------------||||||||2 Dimensional Array||||||||||||||||||-----------------------------------------
# a=np.random.randint(low=0,high=15,size=(3,3))
# print(a)
# # Outputt:-
# [[12  6  6]
#  [ 9  2 13]
#  [ 4 14 14]]
# print(a[[1,2,1],[0,1,2]])
# [ 9 14 13]


# a=np.array([[1,-2,3],[4,-2,3]])
# print(a[a<0])
