# #Ques:
# #To find the max distance between the same numbers in a list
# n=list(input().split())
# #print(n) 5 2 3 25 3 256 2 6 5 2
# count=0
# for _ in n:
#     for i in _:
#         if _==i:
#             print(_.index(i))
# |My Trail

# print("----------------------------------------------------")

# |||||||ChatGPT|||||||| FOR FINDING 1ST MAX DIS
# n = list(map(int, input().split()))  # Convert input to a list of integers
# max_distance = 0

# for i in range(len(n)):
#     for j in range(i+1, len(n)):
#         if n[i] == n[j]:
#             distance = j - i
#             max_distance = max(max_distance, distance)
#         print("Maximum distance between same numbers:", max_distance)

# print("----------------------------------------------------")

#FOE FINDING THE SECOND MAX DIS
n=list(map(int,input().split()))
dis=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            distance=j-i
            dis.append(distance)
dis=list(set(dis))
print(max(dis))
dis.sort(reverse=True)
print(dis)
Sec_Max_Dis=dis[1]
print(Sec_Max_Dis)