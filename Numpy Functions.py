import numpy as np
# a=(np.array([3,6,12,15,18]))
# print(np.array(a/3))
# print("----------------------------------------------------------------------------------------")


# 2.numpy.arange
# print(np.arange(1,20))
# print(np.arange(1,20,3))
# print(np.arange(1,20,2,float))#or dtype="float"
# print("----------------------------------------------------------------------------------------")


# # 3.numpy.zero
# print(np.zeros(5)) #Output=[0. 0. 0. 0. 0.]
# print(np.zeros(5,int))#or dtype="int"   Output=[0 0 0 0 0]
# print(np.zeros((2,4),dtype=int))#(2=2 rows, 4= 4 columns)
# print("----------------------------------------------------------------------------------------")


# # 4.numpy.ones
# print(np.ones(5,int))#Output=[1,1,1,1,1]
# print(np.ones((2,3),int))#Output=[[1,1,1]
# #                             [1,1,1]]
# print(np.empty(3,int))#Output=[6684783 7798900 7471201] (Prints some random numbers)
# print(np.empty((2,3),int))#[[1 0 8]
#                     #    [0 8 0]]
# print("----------------------------------------------------------------------------------------")


# # 5.numpy.linspace  (If num="Not Specified", In output we'll get 50 values because num default value is 50)
# print(np.linspace(1,20,num=5,dtype=int))#Output=[ 1  5 10 15 20]
# print(np.linspace(1,20,num=5,endpoint=False,dtype=int))#Output=[ 1  4  8 12 16]
# print(np.linspace(1,20,num=5,dtype=int,retstep=True))#Output=(array([ 1,  5, 10, 15, 20]), 4.75)
# print(np.linspace(1,20,num=5,dtype=int,endpoint=False,retstep=True))#Output=(array([ 1,  4,  8, 12, 16]), 3.8)

# 6.numpy.eye  (or)   numpy.identity
# print(np.eye(5))
# # OUTPUT:-
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

# print(np.eye(2,3))
# # Output:-
# [[1. 0. 0.]
#  [0. 1. 0.]]

# print(np.eye(3,k=1))           #print(np.eye(3,3,k=-1))
# # Output:-              
# [[0. 1. 0.]               [[0. 0. 0.]
#  [0. 0. 1.]                [1. 0. 0.]
#  [0. 0. 0.]]               [0. 1. 0.]]

# print(np.eye(5,k=2))
# Output:-
# [[0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

# print("----------------------------------------------------------------------------------------")

# 7.numpy.random
# # Modules=rand(),  randn(), ranf(),  randint()
# print(np.random.rand(1,5))#Output:-[[0.47519832 0.56466166 0.70830217 0.5647063  0.67941825]]
# print(np.random.randn(1,5))
# print(np.random.randint(1,5))#Output:-(A Random number between 1 to 5)
# print(np.random.randint(low=0,high=25,size=(2,5))#Output:-(Creates a Matrix within the range of 0,25 and in 2 rows & 3 Cols)
# print(a)
# a=np.random.randint(low=0,high=7,size=(2,3))
# print(a)
# print(a[1][2])
# print("----------------------------------------------------------------------------------------")

