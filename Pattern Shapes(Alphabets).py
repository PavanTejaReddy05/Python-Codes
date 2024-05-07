str=input("Enter the Str (Python): ")
length=len(str)
for i in range(length):
    for j in range(i+1):
        print(str[j], end=" ")
    print()