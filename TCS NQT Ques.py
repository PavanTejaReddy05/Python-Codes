n=[]

for i in range(5):
    Fruit=input("Enter the Fruit: ")
    Quantity=int(input("Enter the Number of Quantity's: "))
    Cost_of_Each_Quantity=int(input("Enter the Cost_of_Each_Quantity: "))
    n.append((Fruit,Quantity,Cost_of_Each_Quantity))

'''
Input:
Fruit,Quantity,Cost of each Quantity: Oranges,5,20
Fruit,Quantity,Cost of each Quantity: Apples,8,25
Fruit,Quantity,Cost of each Quantity: Bananas,12,7
Fruit,Quantity,Cost of each Quantity: PineAplle,3,30
Fruit,Quantity,Cost of each Quantity: Pappaya,6,24

Output:
Total Sale of the Day:-618
Average Sale of the Day:-124
Highest Saled Fruit:-Bananas'''
# print(n)
# n = [('Orna', 5, 20), ('aplle', 8, 25), ('bana', 12, 7), ('pine', 3, 30), ('papa', 6, 24)]

Total_Sale=0                                                     #|res = []
for Fruit,Quantity,Cost_of_Each_Quantity in n:                   #|for _ in range(3):
    Total_Sale=+Total_Sale+(Quantity*Cost_of_Each_Quantity)      #|  n = tuple(input().split())
print(Total_Sale)                                                #|  res.append(n)                                                 
Avg_Sale=Total_Sale/5                                            #|print(res)
print("Average Sale of the Day:-",Avg_Sale)
High_Sale=max(n,key=lambda x:x[1])
print("Highest Saled Fruit:-",High_Sale[0])
# High_Sale=max(n,key=lambda x:x[1][0])
# print("Highest Saled Fruit:-",High_Sale)