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