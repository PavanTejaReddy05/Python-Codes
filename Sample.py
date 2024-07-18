n=int(input("Enter the value: "))
# # for i in range(1,n+1):
# #     for j in range(1,i+1):
# #         print(j,end=" ")
# #     print()
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num=num+1
#     print()

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i, end=" ")
    print()