n="Hello"
'''Rev=n[::-1]
print(Rev)'''
rev_str=''
for i in n:
    rev_str=i+rev_str
    print(rev_str)

x=""                                      #Input=Pavan
for i in n:                               #Output=navaP
    x=i+x

res = [('orange', '12', '45'), ('apple', '45', '7'), ('banana', '7', '8')]

a = res[0][1]
a = int(a)

b = res[0][2]
b = int(b)
print(a*b)

print(int(res[0][1])*int(res[0][2]))

lst = ['Benevolent', 'Dictator', 'For', 'Life']
# st=[sorted(lst) for i in lst]
# print(st[0])
print(sorted(lst))
# string=""
print(" ".join(lst))