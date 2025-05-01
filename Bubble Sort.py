# lst=list(map(int,input().split(",")))

# for i in range(len(lst)):
#     for j in range(0,len(lst)-i-1):
#         if lst[j]>lst[j+1]:
#             lst[j],lst[j+1]=lst[j+1],lst[j]
# print("Sorted List is",lst)
num=6
val=1
for i in range(2,num+1):
    val=i*val
print(val)