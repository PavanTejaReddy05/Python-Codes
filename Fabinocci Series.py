n=int(input("Enter the value: ")) 
a=0                     #first=0
b=1                     #second=1
for i in range(n):
    print(a)            #print(first)
    q=a                 #temp=first
    a=b                 #first=second
    b=q+b               #second=temp+second