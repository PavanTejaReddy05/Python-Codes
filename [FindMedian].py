num1=list(map(int,input().split(",")))
num2=list(map(int,input().split(",")))
# print(num1,num2)
m_lst=num1+num2
m_lst.sort()
n=len(m_lst)
if n%2==0:
    median=(m_lst[n//2-1]+m_lst[n//2])/2
else:
    median=m_lst[n//2]
print(median)        