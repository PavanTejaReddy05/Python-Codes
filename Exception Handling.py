lst=list(map(int,input("Enter the list: ").split()))
# l=[try i**2 for i in lst if i>=0 else raise ValueError i,"Num is Neg Num" except ValueErroras as ve ]
for i in lst:
    try:
        if i>=0:
            print(i**2)
        else:
            raise ValueError(i,"Num is Neg Num")
        
    except ValueError as ve:
        print(ve)
########################################################################################################
while True:
    try:
        n=int(input("Enter The Number: "))
        break
    except ValueError:
        print("Give Value Type is not a Int")
print("Now the given value",n,"is int type")