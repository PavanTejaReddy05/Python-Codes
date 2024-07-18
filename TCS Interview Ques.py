a=int(input("Enter the Val: "))
b=int(input("Enter the VAl: "))
for i in range(a,b+1):
    for j in range(0, b-a+1):
        num=i+j
        if num>b:
            num=num-b
        print(num, end=" ")
    print()