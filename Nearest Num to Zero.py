lst=[1,-2,-6,12,32,16,128,-658,-43,55]
neg=[]
pos=[]
for i in lst:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
pos.sort()
neg.sort(reverse=True)
# print(neg,pos)
for i,j in zip(neg,pos):
    print(i,j)
    if abs(i)<abs(j):
        print(i)
        break
    else:
        print(j)
        break