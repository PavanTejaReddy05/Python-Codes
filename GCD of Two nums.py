a=16
b=32
# lst=[]
# for i in range(1,a+1):
#     if a%i==0:
#         lst.append(i)

# lst1=[]
# for i in range(1,b+1):
#     if b%i==0:
#         lst1.append(i)

# lst2=[]
# for i in lst:
#     if i in lst1:
#         lst2.append(i)

lst=[i for i in range(1,a+1) if a%i==0]
lst1=[i for i in range(1,i+1) if a%i==0]
lst2=[i for i in lst if i in lst1]
print(f"GCD of {a},{b} is {max(lst2)}")