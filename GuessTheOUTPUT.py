# x=[]
# if x:
#     print(x,"True")
# else:
#     print(x,"False")
#   # Output=False Because x is empty

# print("----------------------------------------------------")

# p=(1,10)
# q=0
# r=[]
# if p or q and r:
#     print("True")
#     # Output=True

# print("----------------------------------------------------")

# lst=["ABC","XYZ","pqR"]
# for i in lst:
#     i.lower()   #OUTPUT=lst["ABC","XYZ","pqR"]
# print(lst) 

# print("----------------------------------------------------")

# lst=["ABC","XYZ","pqR"]
# lst1=[]
# for i in lst:
#     x=i.lower()
#     lst1.append(x)
# print(lst) #OUTPUT=lst1=["abc","xyz","pqr"]

# print("----------------------------------------------------")

# lst=["ABC","XYZ","pqR"]
# for i in lst:
#     lst.append(i)#OUTPUT=No Output because loop doesn't have break point
# print(lst)

# print("----------------------------------------------------")

# for i in range(1,20):
#     if i==5:
#         break
#     else:
#         print(i)
# else:
#     print("Hello")
# Output=1,2,3,4

# print("----------------------------------------------------")

# lst=["A","b","c",["d","elephant"],"f","g","h"]
# print(lst[3:4]) 
# print(lst[3:4][0])#or print(lst[3])
# print(lst[3:4][0][1][2])#[0]=d,"elephant"
#                         #[1]="elephant"
#                         #[2]=e

# print("----------------------------------------------------")

# def func(n,list=[]):
#     list.append(list.append(n))
#     return list
# for i in range(4):
#     lst2=func(i)
# print(lst2)
# Output=[0, None, 1, None, 2, None, 3, None]
# For explanation (Amulya Academy,Playlist="Guess the Output",7th Video)

# print("----------------------------------------------------")

# for i in [20,10,3,4][::-1]:
#     print(i)                      #Output=4 3 10 20


# for i in sorted([20,10,3,4]):
#     print(i)                         #Output=3 4 10 20

# for i in sorted([20,10,3,4],reverse=True):
#     print(i)                       #Output=20 10 4 3

# print("----------------------------------------------------")

# a={}
# a[1]=1
# a["1"]=2
# a[1]=a[1]+2
# a["a"]=a["1"]+3
#                          #{3,2,5}
# count=0
# for i in a:
#     count=count+a[i]         #{1:3,'1':2,'a':5}
# print(a)
# print(count)                 #Output=3+2+5=10

# print("----------------------------------------------------")

# str="Welcome to Python"
# i="Py"
# while i in str:
#     print(i,end="")
#     break
# else:
#     print("None")

# print("----------------------------------------------------")

# lst1=[1,2,3]
# lst2=[[i for i in lst1]for i in range(4)]
# print(lst2)

# print("----------------------------------------------------")

# str1="hello world"
# while str1:
#     print("hello")
#     str1=str1[1::2]
#     # output:hello 4 times

# print("----------------------------------------------------")

#Ques:
# To Print the numbers from 71 to 81 without using numbers
# ASCII Values A=65, B=66, C=67.......

# for i in range(ord("G"),ord("Q")):
#     print(i)

# print("----------------------------------------------------")

