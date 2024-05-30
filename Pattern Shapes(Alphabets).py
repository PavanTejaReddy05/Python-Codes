str=input("Enter the Str (Python): ")
length=len(str)
for i in range(length):
    for j in range(i+1):
        print(str[j], end=" ")
<<<<<<< HEAD
    print()

# print("----------------------------------------------------------------------------------------")
n,m=map(int,input("Enter the n,m Values with space:").split())

for i in range(1,n//2+1):
    pattern=".|."*(2*i-1)
    print(pattern.center(m,"-"))

print("Welcome".center(m,"-"))

for i in range(n//2,0,-1):
    pattern=".|."*(2*i-1)
    print(pattern.center(m,"-"))
'''OUTPUT
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------'''
=======
    print()
>>>>>>> 536510fcd2b1405bbd180520ae4284d1dedd36f9
