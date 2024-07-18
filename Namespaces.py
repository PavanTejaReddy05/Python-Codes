# def func1():
#     a=60
#     print(id(a))
#     print(a)

#     def func2():
#         a=35
#         print(id(a))
#         print(a)
#     func2()
# func1()
# # print("----------------------------------------------------------------------------------------")
a=1
b=2
c=3
globals( )["a"]=12
globals( )["b"]=13
globals( )["c"]=15
print(a)
print(b)
print(c)