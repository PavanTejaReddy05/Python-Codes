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
        print("It is not a Palindrome") 

