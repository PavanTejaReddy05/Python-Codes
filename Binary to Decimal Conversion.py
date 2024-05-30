n = str(input("Enter the binary number: "))
decimal = 0

# Iterate over each digit of the binary number
for i in range(len(n)):
    # Convert the current digit to an integer
    digit = int(n[i])
    # Calculate the positional value and add it to the decimal sum
    decimal += digit * (2 ** (len(n) - 1 - i))
    print("Decimal equivalent:", decimal)

# Print the decimal equivalent
# print("----------------------------------------------------------------------------------------")
'''Binary representation of 10 is 1010.
After toggling the bits(1010), will get 0101 which represents “5”. 
Hence output will print “5”.'''
n=int(input("Enter the number: "))
x=str(bin(n))
# print(x)#0b1010
x=x[2:]#1010
# print(x)
l=""
for i in x:
    # print(i)
    if int(i)==0:
        l=l+"1"
    else:
        l=l+"0"
# print(l) 
print(int(l,2))#converts the binary number to decimal