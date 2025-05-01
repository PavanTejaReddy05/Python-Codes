n=int(input("Enter the value: ")) 
a,b=0,1
for _ in range(n):
    print(a)
    a,b=b,a + b   #(a,b)=(b,a)+b


#Approach :2

n=15
a=0                     #first=0
b=1                     #second=1
for i in range(n):
    print(a)            #print(first)
    q=a                 #temp=first
    a=b                 #first=second
    b=q+b               #second=temp+second