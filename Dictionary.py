Car={"Suzuki":("Amaze","Baleno"),"Honda":"Crysta","Mahindra":("TUV","XUV")}
# for key in Car.values():
#     print((key))
print(*Car["Suzuki"])
print()
for k, v in Car.items( ) :
    if k=="Suzuki" and v==("Amaze","Baleno"):
        print(k,":", *v)# iterate over keys 
    elif k=="Mahindra" and v==("TUV","XUV"):
        print(k,":", *v)
    else:
        print( k,":", v)
print()
for k in enumerate(Car.keys( )):
    print(*k)# iterate over keys - shorter way
print()
for k in Car:
    print(k)
print()
for v in Car.values( ) :
    if v==("Amaze","Baleno"):
        print(*v)
    elif k=="Mahindra" and v==("TUV","XUV"):
        print(*v)
    else:
        print(v)
print()
'''-------------------------------------------------REVERSE OPERATION--------------------------------'''
c=sorted(Car)
print(*c)    #Honda Mahindra Suzuki
print()
for k,v in reversed(Car.items()):
    print(k,v)


print()


animals = {'Tiger' : 141, 'Lion' : 152, 'Leopard' : 110}
birds = {'Eagle' : 38, 'Crow': 3, 'Parrot' : 2}
combinations={**animals,**birds}
for i in combinations.items():
    print(*i)


print()

lst=["Pavan","Theja","Vinni"]
length=5
d=dict.fromkeys(lst,5)
print(d)
print()

import operator
d={"Oil":230, "Clip":150, "Stud":175, "Nut":35}
print("Original dictionary: ",d)
print()
d1=sorted(d.items(),key=operator.itemgetter(1))
print(d1)
print()


'''Write a program to create three dictionaries and concatenate them to create fourth dictionary.'''
d1 = {'Mango' : 30, 'Guava': 20}
d2 = {'Apple' : 70, 'Pineapple' : 50}
d3 = {'Kiwi' : 90, 'Banana' : 35}
d4 = { }
# for i in (d1,d2,d3):
#     d4.update(i)
# print(d4)
'''--------------or-----------'''
d4={**d1,**d2,**d3}
print(d4)
print("Sorted according to values using itemgetter")
d=sorted(d4.items(),key=operator.itemgetter(1))
print(d)
print()
print()
d1 = {'Anil' : 45, 'Amol' : 32}
if bool(d1) :
    print('Dictionary is not empty')
d2 = { }
if not bool(d2) :
    print('Dictionary is empty')
else:
    print("Dictionary is not empty")

'''Suppose  there  are  two  dictionaries  called  boys and  girls containing names as keys and ages as values. 
Write a program to  merge the two dictionaries into a third dictionary'''
boys = {'Nilesh' : 41, 'Soumitra' : 42, 'Nadeem' : 47}
girls = {'Rasika' : 38, 'Rajashree': 43, 'Rasika' : 45}
merg={}
# for i in (boys,girls):
    # merg.update(i)
# print(merg)
merg={**boys,**girls}
print(merg)

'''Suppose  a  dictionary  contains  roll  numbers  and  names  of  students. 
Write  a  program  to  receive  the  roll  number,  
extract  the  name corresponding to the roll number and display a message congratulating the  student  by  his  name.  
If  the  roll  number  doesn't  exist  in  the dictionary, 
the message should be 'Congratulations Student!'''
students = {554 : 'Ajay', 350: 'Ramesh', 395: 'Rakesh'}
n=int(input())
name=students.get(n)
if name:
    print("Congratulations",name)
else:
    print("Congratulations Student!!!")
############################################################################################
four_Wheeler={"Suzuki":("Waganor","Swift","Baleno","Breeza","Amaze"),"Mahindra":"TUV","Huyndai":"Nios i10"}
for i,j in four_Wheeler.items():
    if isinstance(j,tuple):
        l=list(j)
        # k=sorted(l)
        # print(k)
        print(i,":",",".join(sorted(l)))
    else:
        print(i,":",j)
###################################################################################################

l=[chr(i) for i in range(65,90+1)]
n=[i for i in range(1,26)]
dictionary=dict(zip(l,n))
print(dictionary)
############################################################################################
dict1={"A":1,"B":2,"C":3}
dict2={"a":4,"b":5,"c":6}
print(dict1|dict2)
################################################################################################
mgdict={**dict1,**dict2}
print(mgdict)
print(dictionary)
