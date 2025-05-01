import numpy as np
lst=[1, 2, 3, 4]
# op=[24, 12, 8, 6]
lst1=[]
for i in range(len(lst)):
    a=np.prod(lst[:i])
    b=np.prod(lst[i+1:])
    c=a*b
    lst1.append(int(c))
print(lst1)