a=[int(x) for x in range(0,10)]
print(a)

import random
b=[random.randint(10,100) for x in range(0,10)]
print(b)

c=[int(x) for x in ['10','20','30','40']]
print(type(c))

d=[(x,x**2,x**3) for x in range(0,10)]
print(d)

e=[i for i in range(0,10) if i%2==0]
print(e)

l=[1,12,15,8,6,22,20,26,32,63,52,19,17,5,4]
f=[i for i in l if i<20 or i>50]
print(f)

g=["!" if i in "aeiou" else i for i in "Technical"]
print(g)

'''Using list comprehension, 
write a program to generate a list of numbersin the range 2 to 50 that are divisible by 2 and 4'''
a=[i for i in range(2,50) if i%2==0 and i%4==0]
print(a)

'''Write a program to flatten the following list using list comprehension:
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]'''
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
a=[j for i in mat for j in i]
print(a)


"""
Write  a  program  
to  create  a  set  containing  some  randomly  generated numbers  in  the range  15 to  45. 
Count  how  many of these  numbers  are less than 30. 
Delete all numbers which are less than 30."""

import numpy as np
x=np.random.randint(15,45,8)
# l=tuple(*l)
print(x)
count=sum(1 for i in x if i>=30)
a=[i for i in x if i>=30]
print(count)
print(a)

names = ['Sunil', 'Sachin', 'Rahul', 'Kapil', 'Rohit']
marks = [54, 65, 45, 67, 78]
dict=dict(zip(names,marks))
dic={k:v for (k,v) in zip(names,marks)}
print(dic)
print(dict)