'''Output Format:-
Print the name(s) of any student(s) having the second lowest grade in. 
If there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input 0:-
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0:-
Berry
Harry'''
n=int(input())
l=[]
for _ in range(n):
    name=input()
    score=float(input())
    l.append((name,score))

l.sort(key=lambda x:x[1])     #[('Tina', 37.2), ('Harry', 37.21), ('Berry', 37.21), ('Harsh', 39.0), ('Akriti', 41.0)]
# print(l)
l.pop(0)                      #[('Harry', 37.21), ('Berry', 37.21), ('Harsh', 39.0), ('Akriti', 41.0)]
# print(l)
marks = l[0][1]               #l[0][1]=37.21

l.sort(key= lambda x:x[0])    #[('Akriti', 41.0), ('Berry', 37.21), ('Harry', 37.21), ('Harsh', 39.0)]
# print(l)
for i in l:
    if(i[1] == marks):
        print(i[0],end="\n")
