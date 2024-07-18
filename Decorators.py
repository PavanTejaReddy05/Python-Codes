def decorator(func):
    def Hiphens(n):
        print(n*"-")
        func(n)
    return Hiphens

@decorator
def name(n):
    print("Pavan Teja")

n=int(input("Enter the val: "))
name(n)

############################################################################################
def func1(a):
    def ChkEve(x,y):
        if x%2==0 and y%2==0:
            a(x,y)
        else:
            print("Give the Even Numbers")
    return ChkEve

@func1
def sum(a,b):
    print(a+b)

a,b=map(int,input("Enter the a,b Vals: ").split())
sum(a,b)