# if _name_ == '_main_':
n=input()#Hello World
x=n.lower()
print(x)
count=0
for i in x:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        count=count+1
print(count)