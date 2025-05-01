s="{[()]}"
stack=[]
data={")":"(","]":"[",")":"("}
for i in s:
    if i in data.values():
        stack.append(i)
    elif i in data:
        if not stack or stack[-1]!=data[i]:
            return False
        stack.pop()
if stack :
    print("Brackets are Balanced")
else:
    print("Brackets aren't Balanced")