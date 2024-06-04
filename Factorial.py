import math
n=int(input("Enter the value: "))
f=1
for i in range(1,n+1):
    f=i*f
print(f)

print("--------------------------------------")
######################################################################################

fact=(n*math.factorial(n-1))
print(fact)
######################################################################################


result=math.factorial(n)
print("The Facrorial for the value {} is {}" .format(n,result))
########################################################################################
def refact(n):
    if n == 0:
        return 1
    else:
        return n * refact(n - 1)

result = refact(5)
print(result)  # Output will be 120