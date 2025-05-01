#  factorial calculation,
#  Fibonacci sequence,
#  summing numbers,
#  reversing a string,
#  and checking for palindromes.


name="Pavan Teja Reddy"
def vwls(string):
    count=0
    string=set(string)
    print(string)
    # string=string.lower()
    for i in string:
        if i in "aeiou":
            count=count+1
    return count
print("Count of vowels in string is ",vwls(name))


# number=163
# def Armstrong(n):
#     sum=0
#     for i in str(number):
#         sum=sum+int(i)**len(str(number))
#     return sum
# print(Armstrong(number))

# a=0
# b=1
# for i in range(1,10):
#     print(a)
#     a,b=b,a+b

# lst=[12,15,133,14,23,28,24,63,100]
# print(max(lst))

# word="Dad"
# def pal(word):
#     word=word.lower()
#     return word

# print(pal(word)[::-1] == word.lower())



# number=3
# def fact(n):
#     a=1
#     for i in range(2,number+1):
#         a=i*a
#     return a
# print(fact(number))

# def prime(number):
#     if number<=1:
#         return False
#     for i in range(2,int(number**0.5)+1):
#         if number%i==0:
#             return False
#     return True

# print(prime(number))

lst=[12,15,133,14,23,28,24,63,100]
def secL(lst):
    maxNum=max(lst)
    lst.remove(maxNum)
    print(lst)
    SecMaXNum=max(lst)
    return SecMaXNum
print(secL(lst))
