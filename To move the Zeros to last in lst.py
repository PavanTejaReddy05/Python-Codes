# lst=[-1,5,0,6,4,0,3,0]
# Output:[-1,5,6,4,3,0,0,0]
# non_zero_count=0
# for i in range(len(lst)):
#     if lst[i]!=0:
#         lst[non_zero_count]=lst[i]
#         non_zero_count=+1

# for i in range(non_zero_count,len(lst)):
#     lst[i]=0
# print("----------------------------------------------------------------------------------------")
# otpt=lst
# otpt=list(filter(lambda x:x!=0, lst))
# otpt.extend([0]*lst.count(0))
# print(otpt)
# print("----------------------------------------------------------------------------------------")
l=list(map(int, input("Enter the list: ").split(",")))
non_zero_end=len(l)-1
i=0
while i<non_zero_end:
    if l[i]==0:
        l[i],l[non_zero_end]=l[non_zero_end],l[i]
        non_zero_end-=1
    else:
        i=i+1
print(l)