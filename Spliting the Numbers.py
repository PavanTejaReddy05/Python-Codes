'''(Done by me = Mistake)
num=int(input())
while num!=0:
    initial=num%10
    n=num//10
    print(n)
'''
n = int(input("Enter an integer: "))
while n > 0:
    digit = n % 10
    print(digit)
    n = n // 10
