# res = []
# for _ in range(3):
#     n=tuple(input().split())
#     res.append(n)
# print(res)

res = [('orange', '12', '45'), ('apple', '45', '7'), ('banana', '7', '8')]

a = res[0][1]
a = int(a)

b = res[0][2]
b = int(b)
print(a*b)

print(int(res[0][1])*int(res[0][2]))