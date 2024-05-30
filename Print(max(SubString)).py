# s=input()
# l=[]
# for i in range(len(s)):
#     for j in range(i+1,len(s)):
#         if i!=j:
#             l.append(i,i[0])
#         else:
#             continue
# f=max(l,len(i))

s = input()
longest_substring = ""
max_length = 0

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):  
        substring = s[i:j]
        if len(set(substring)) == len(substring):  
            if len(substring) > max_length:
                max_length = len(substring)
                longest_substring = substring

print(longest_substring) 
