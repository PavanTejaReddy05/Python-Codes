# import keyword
# print(keyword.kwlist)
# print("----------------------------------------------------------------------------------------")
# import math
# print(dir(__builtins__))
# print(dir(math))
# print("----------------------------------------------------------------------------------------")
# result = divmod(20, 5)
# print(result)  # Output: (4, 0)
# 20 divided by 5 is 4 with no remainder.
# print("----------------------------------------------------------------------------------------")
# result = math.modf(10.67)
# print(result)  # Output: (0.6700000000000004, 10.0)

# # Example 2: Splitting a negative float
# result = math.modf(-10.67)
# print(result)  # Output: (-0.6700000000000004, -10.0)
# print("----------------------------------------------------------------------------------------")
'''Create  a  list  of  tuples.  
Each  tuple  should  contain  an  item  and  its price in float. 
Write a program to sort the tuples in descending order by price. 
Hint: Use operator.itemgetter( )'''
# import operator
# lst=[("Apple",12),("Banana",7),("Carrot",8),("DryFruits",16),("Pappaya",25)]
# for i in lst:
#     lst1=sorted(lst, key=operator.itemgetter(1), reverse=True)
# print(lst1) 
########################################################################################################
# def fun(num) :
#     if num == 0 :
#         print("False")
#     if num == 1 :
#         print("True")
#     if num % 2 == 0 :
#         fun(num / 2)
# fun(256)

###########################################################################################################
def fun(n) :
    if n % 5 == 0 :
        return True
    else :
        return False
lst1 = ['A', 'X', 'Y', '3', 'M', '4', 'D']
f1 = filter(str.isalpha, lst1)
print(list(f1)) # prints ['A', 'X', 'Y', 'M', 'D']
lst2 = [5, 10, 18, 27, 25]
f2 = filter(fun, lst2)
print(list(f2)) # prints  [5, 10, 25]

#########################################################################################################33
l=[1,2,3,4,5,6]
l1=[6,5,4,1,2,3]
resulr=list(map(lambda x,x1:x+x1,l,l1))
print(resulr)
##########################################################################################################
d = {'x' : 500, 'y' : 5874, 'z' : 560}
# l=[]
# for i in d.values():
#     l.append(i)
# l=[i for i in d.values()]
# print("Maximum Value is",max(l))
# print("Minimum Value is",min(l))
print(max(d.values()))
print(min(d.values()))
###############################################################################################
lst = [10, 20, 30, 40]
i = lst.__iter__( )
print(i.__next__( ))
print(i.__next__( ))
print(i.__next__( ))
lst = [10, 20, 30, 40]
i = iter(lst)
print(next(i))
print(next(i))
print(next(i))

###################################################################################################
import sys
lst = [i * i for i in range(15)]
gen = (i * i for i in range(15))
print(lst)
print(gen)
print(sys.getsizeof(lst))
print(sys.getsizeof(gen))
###################################################################################################
names = ['Amol', 'Anil', 'Akash']
ages = [25, 23, 27]
salaries= [34555.50, 40000.00, 450000.00]
l=list(zip(names,ages,salaries))#[('Amol', 25, 34555.5), ('Anil', 23, 40000.0), ('Akash', 27, 450000.0)]
l=list(zip(names,ages,salaries))
# l1=list(filter(key=lambda x:x[0],l))
l1=[]
l2=[]
l3=[]
for i in l:
    l1.append(i[0])
    l2.append(i[1])
    l3.append(i[2])
print(l)
print(tuple(l1),"\n",tuple(l2),"\n",tuple(l3))
#################################################################################################
# s=" Hi "
# h=s.center(20,"!").strip()
# print(h)
#################################################################################################
n=int(input("ENter the value: "))
l=[f"{n}*{i}={n*i}" for i in range(1,11)]
for i in l:
    p=i
print(tuple(l1),"\n",tuple(l2),"\n",tuple(l3))
