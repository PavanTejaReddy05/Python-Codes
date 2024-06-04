# def fun1():
#     print("Reached to function1")
#     def fun2():
#         print("1")
#     print("2")
#     fun2()

# fun1()
# # fun2() "Cannot call Inner func from here"

# print("----------------------------------------------------------------------------------------")
#Multiple input values without having a range or without defing
# def ipt(*args):
#     print()
#     for i in args:
#         print(i,end=" ")
# ipt(input("Enter the Values: "))

# print("----------------------------------------------------------------------------------------")
# def marks(name="Vinni",Marks=55):
#     print(name,Marks)
# dict={'name':"Raju",'Marks': 43}
# marks(*dict)#name Marks
# marks(**dict)#Raju 43
# # marks()#Vinni 55
# print("----------------------------------------------------------------------------------------")

'''Write  a program  to  receive  three  integers  from  keyboard  and  get their sum  and  product  c
alculated  through  a  user-defined  function 
cal_sum_prod( ).'''
def cal_sum_prod(a,b,c):
    sum=a+b+c
    print(sum)
    product=a*b*c
    print(product)
cal_sum_prod(a=int(input("Enter")),b=int(input("Enter")),c=int(input("Enter")))

# print("----------------------------------------------------------------------------------------")
'''Write  a  Python  program  that  accepts  a  hyphen-separated  sequence  of words  
as  input  and  calls a  function  convert( ) which  converts  it  into  a hyphen-separated  sequence  
after  sorting  them  alphabetically. 
For example, if the 
input string is 
'here-come-the-dots-followed-by-dashes'then, 
the converted string should be
'by-come-dashes-dots-followed-here-the'''
# Page No:182,166
# _________________This is my code____________________________
def hephSep(s):
    s=s.replace("-"," ")
    s=s.split()
    lst=[]
    for i in s:
        lst.append(i)
    lst.sort()
    # print(lst)
    st=""
    # st=str(st)
    for i in lst:
        st=st+"-"+i
    st=st.strip("-")
    print(st)
hephSep("here-come-the-dots-followed-by-dashes")
#______________________________________________________________#
def convert(s1) :
    items = [s for s in s1.split('-')]
    items.sort( )
    s2 = '-'.join(items)
    return s2 
s = 'here-come-the-dots-followed-by-dashes'
t = convert(s)
print(t)

# print("----------------------------------------------------------------------------------------")
'''Write a  Python function  to  create and  
return a  list containing  tuples  of the form (x, x2, x3) 
for all x between 1 and 20 (both included)'''
def tup(a,b):
    # lst=[]
    # for i in range(a,b+1):
    #     lst.append((i,i**2,i**3))
    lst=[(i,i**2,i**3) for i in range(a,b+1)]
    print(lst)
tup(1,10)
# print("----------------------------------------------------------------------------------------")
'''A  palindrome  is  a  word  or  phrase  which  reads  the  same  in  both directions. 
Given below are some palindromic 
strings:
deed,level,Malayalam
Rats live on no evil star
Murder for a jar of red rum
Write  a  program  that  defines  a  function  ispalindrome(  ) 
which  checks whether  a  given  string  is  a  palindrome  or  not.  
Ignore  spaces  and  case mismatch while checking for palindrome. 
Program'''
def ispalindrom(s):
    n=s.replace(" ","")
    p=n.lower()
    pal=p[::-1]
    if pal==p:
        print(True)
    else:
        print(False)

ispalindrom(input())
# print("----------------------------------------------------------------------------------------")
