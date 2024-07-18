'''num=int(input("Enter Your Num: "))    |input=153
num=str(num)                             |len(input)=3
pwr=len(num)                             |(1^3)+(5^3)+(3^3)=153=input then it is a Armstrong Number
A=0
while num!=0:
    n=int(num)%10
    n=int(num)//10
    A=A+n**pwr
print(A)'''

num = int(input("Enter Your Num: "))
num_str = str(num)  # Convert the integer input to a string

pwr = len(num_str)  # Calculate the length of the input number

A = 0
for digit in num_str:  # Iterate over each digit in the input number
    n = int(digit)  # Convert the digit back to an integer
    A = A + n ** pwr  # Add the power of the digit to the accumulator A
if A==num:
    print("It is a Armstrong Number")

print(A)
