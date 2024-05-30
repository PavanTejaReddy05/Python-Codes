
n=int(input("Enter the value: "))
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            break
    else:
        print(n,"is a Prime Number")
else:
    print(n,"is not a prime number")
'''
n = int(input("Enter the value: "))

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:
        print(n, "is a Prime Number")'''
