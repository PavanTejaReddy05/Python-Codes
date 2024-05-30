'''n=5
for i in range(1,n+1):           |"i" is for rows, "j" is for cols
    for j in range(1,i+1):       |here in j loop 1, "i+1" is because need to print in a format
        print(j,end="")          |
    print()                      |
'''
n=int(input("Enter the value: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


print("-------------------------------------------------")


for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

print("---------------------------------------------------")

num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num=num+1
    print()

print("-----------------------------------------------------")


for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

print("---------------------------------------------------")



for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()