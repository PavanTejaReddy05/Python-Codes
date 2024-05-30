n=int(input())
lst=list(map(int,input().split()))
l=[]
lst.sort()
for i in lst:
    for j in range(i+1,len(lst)):
        val=j-i
        l.append(val)
