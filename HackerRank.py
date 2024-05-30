'''You are given information of N houses, each with price, number of bedrooms, and square footage.
You are asked to calculate two average footages. One for houses with 3 or fewer bedrooms, one for houses with 4 or more bedrooms. It is guaranteed that there exist at least one houses of each kind.

Input Format:-
The first line contains one integer number N, the number of houses.
Each of the next N lines contains 3 integer numbers which are price, number of bedrooms, and square footage.

Output Format:-
Output one line that contains two numbers separated by one whitespace. 
The first number is the average number of square footages for all houses with 3 or fewer bedrooms.
The second is the average number of square footages for all houses with 4 or more bedrooms. 
Use integer division, which rounds down.

Sample Input 0:-
3
100000 3 1000
150999 2 2001
500000 5 3000

Sample Output 0:-
1500 3000'''
n=int(input())
lst=[]
count=0
for _ in range(n):
    cost,roms,sqrft=map(int,input().split())
    lst.append((cost,roms,sqrft))
print(lst)
sum1 = 0
sum2 = 0
count = 0         
for i in lst:#[(100000, 3, 1000), (150999, 2, 2001), (500000, 5, 3000)]
    if i[1]<=3:
        sum1=sum1+i[2]
        count=count+1
    else:
        sum2=sum2+i[2]

avg1 = sum1//count
avg2 = sum2//(len(lst)-count)
print(avg1,avg2)
