n=input("Enter a String to check Whether it is a Palindrome or not: ")
'''
Rev_Str=reversed(n)
if list(n)==list(Rev_Str):
    print("The given String",n,"is a Palindrome")
else:
    print("It is not a Palindrome")
'''
print("-----------------------------------------------------------")
x=""                                      #Input=Pavan
for i in n:                               #Output=navaP
    x=i+x
if x==n:
        print("The Given String {} is a Palindrome.".format(n))
else:
<<<<<<< HEAD
        print("It is not a Palindrome")
print("----------------------------------------------------------------------------------------")

x=input()
low=x.lower()
rev=low[::-1]
if x==rev:
    print(x,"is a Palindrome")
=======
        print("It is not a Palindrome") 

>>>>>>> 536510fcd2b1405bbd180520ae4284d1dedd36f9
