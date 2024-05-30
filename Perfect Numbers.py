#Perfect Numbers
#6 can be divisible by 1,2,3,6
#So sum of Divisors =1+2+3+6=6 So 6 is a Perfect Number
'''n=int(input("Enter the Perfect Number value: "))
l=[]
P=0
for i in range(1,n+1):
    if n%i==0 and i!=n:
        l.append(i)
for i in l:
    P=i+P

print(P,"is a Perfect Number")'''
'''n = int(input("Enter the value: "))
factors = []


for i in range(1, n):
    if n % i == 0:
        factors.append(i)


sum_of_factors = sum(factors)


if sum_of_factors == n:
    print(n, "is a perfect number.")
else:
    print(n, "is not a perfect number.")
'''
Llimit=int(input("Enter the LowerLimit Value: "))
Ulimit=int(input("Enter the UpperLimit Value: "))

for num in range(Llimit,Ulimit+1):
     l=[]
     for i in range(1,num):
        if num%i==0:
            l.append(i)
            if sum(l)==num:
                print(num,"Is a Perfect Number")

