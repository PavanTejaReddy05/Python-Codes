# def nums(s):
#     if s==0:
#         result=0
#     else:
#         nums(s-1)
#     print(s)
# nums(10)
# #################################################################
'''printing 1st 25 nums'''
def num(s):
    if s==0:
        return s
    else:
        num(s-1)
        print(s)
num(25)
####################################################################
'''To print the prime factors in recursive func'''
def pmfac(num,i):
    if i<=num:
        if num%i==0:
            print(i,end=" ")
            num=num//i
        else:
            i=i+1
        pmfac(num,i)

pmfac(50,2)
#############################################################
'''Sum of 1st 25 nums in Recursive Func '''
def sum_1st_nnums(n):
    if n==0:
        return 0
    else:
        return n+sum_1st_nnums(n-1)
    

result=sum_1st_nnums(25)
print(result)
################################################################################
'''Two  numbers  are  received  through  the  keyboard  into  variables  a
and b. Write a recursive function that calculate the value of a**b'''
def pow(a,b):
    if b==0:
        return 1
    else:
        return a*pow(a,b-1)
res=pow(2,3)
print(res)
###############################################################################
'''Reverse the string'''
def rev(l):
    i=0
    if len(l)==0:
        return []
    else:
        return [l[-1]] + rev(l[:-1])

l=list(map(int,input().split()))
res=rev(l)
print(res)
########################################################################
'''fun(4, 2) returns fun(3, 4 * 2).
fun(3, 4 * 2) returns fun(2, 3 * 4 * 2).
fun(2, 3 * 4 * 2) returns fun(1, 2 * 3 * 4 * 2).
fun(1, 2 * 3 * 4 * 2) returns fun(0, 1 * 2 * 3 * 4 * 2).
fun(0, 1 * 2 * 3 * 4 * 2) returns 1 * 2 * 3 * 4 * 2, which equals 48.'''
def fun(x, y) :
    if x == 0 :
        return y
    else :
        return fun(x - 1, x * y)
print(fun(4, 2))
####################################################################################