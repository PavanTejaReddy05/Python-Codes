# i=0
# while i<=10:
#     if i==10:
#         print(i)
#         break
#     print(i, end="-")
#     i+=1
i=1
while i<=3:
    j=1
    while j<=3:
        k=1
        while k<=3:
            if i==j or j==k or k==i:
                k+=1
                continue
            else:
                print(i,j,k)
            k+=1
        j+=1
    i+=1
 # print("----------------------------------------------------------------------------------------")   
i=1
count=0
n=int(input())
while i<=n:
    if n%i==0:
        count+=1
    i=i+1
if count==2:
    print(n,"is prime"  )
else:
    print(n,"is not prime")
    
