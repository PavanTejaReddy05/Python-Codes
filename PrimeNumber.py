
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

max=int(input("Enter the val: "))
for num in range(1,max):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,"is a prime number")