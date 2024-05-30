Top=int(input("No. of Top rankers do u need: "))
Students=int(input("Enter the Total No_Of Students: "))
list=[]
for _ in range(Students):
    Name=input("Enter the Name of the Student: ")
    Score=int(input("Enter the Socre gained by the student: "))
    list.append((Name,Score))
# print(list)->>[('Bob', 82), ('Jack', 92), ('Sai', 84), ('Pavan', 98), ('Leela', 58)]
sorted_list=sorted(list, key=lambda x: x[1], reverse=True)

print("1st Highest Scored Student is",sorted_list[0])
print("2nd Highest Scored Student is",sorted_list[1])
print("3rd Highest Scored Student is",sorted_list[2])
# for i in range(Top):
#     print(i+1,"Highest Scored Student is",sorted_list[i])