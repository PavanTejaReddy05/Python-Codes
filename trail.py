# '''Input:
# Fruit,Quantity,Cost of each Quantity: Oranges,5,20
# Fruit,Quantity,Cost of each Quantity: Apples,8,25
# Fruit,Quantity,Cost of each Quantity: Bananas,12,7
# Fruit,Quantity,Cost of each Quantity: PineAplle,3,30
# Fruit,Quantity,Cost of each Quantity: Pappaya,6,24

# Output:
# Total Sale of the Day:-618
# Average Sale of the Day:-124
# Highest Saled Fruit:-Bananas'''
# # lst=[]
# # for _ in range(5):
# #     Fruit=input("Enter the Fruit Name: ")
# #     Quantity=int(input("Enter the Number of Quantity: "))
# #     Cost_Of_Each_Quantity=int(input("Enter the Cost of Each Quantity: "))
# #     lst.append((Fruit,Quantity,Cost_Of_Each_Quantity))

# # print(lst)
# Total_Sales=0
# lst=[('Oranges', 5, 20), ('Apples', 8, 25), ('Bananas', 12, 7), ('PineApple', 3, 30), ('Pappaya', 6, 24)]
# for i in lst:
#     for j in i:
#         Sales=list[j[1]]*list[j[2]]
#         Total_Sales=Sales+Total_Sales

# print(Total_Sales)


a=4
if not a & 1:
    print("It is a Even Number")
else:
    print("It is a Odd Number")