Fruit,Quantity,Cost_of_each_Quantity="Oranges",5,20
Fruit,Quantity,Cost_of_each_Quantity="Apples",8,25
Fruit,Quantity,Cost_of_each_Quantity="Bananas",12,7
Fruit,Quantity,Cost_of_each_Quantity="PineAplle",3,30
Fruit,Quantity,Cost_of_each_Quantity="Pappaya",6,24
max_sale = max(key=lambda x: x[1])
print("Highest Ssaled Fruit:", max_sale[0])