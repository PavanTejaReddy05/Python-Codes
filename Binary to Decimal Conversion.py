# n = str(input("Enter the binary number: "))
# decimal = 0

# # Iterate over each digit of the binary number
# for i in range(len(n)):
#     # Convert the current digit to an integer
#     digit = int(n[i])
#     # Calculate the positional value and add it to the decimal sum
#     decimal += digit * (2 ** (len(n) - 1 - i))
#     print("Decimal equivalent:", decimal)

# Print the decimal equivalent
# <<<<<<< HEAD
# print("----------------------------------------------------------------------------------------")
'''Binary representation of 10 is 1010.
After toggling the bits(1010), will get 0101 which represents “5”. 
Hence output will print “5”.'''
n=int(input("Enter the number: "))
x=str(format(n,"04b"))
print(x)#0b1010
# x=x[2:]#1010 it is wrong
# print(x)
l=""
'''for i in x:
    # print(i)
    if int(i)==0:
        l=l+"1"
    else:
        l=l+"0"'''
l="".join(["1"if int(i)==0 else "0" for i in x])
print(l) 
print(int(l,2))#converts the binary number to decimal
# =======

# >>>>>>> 536510fcd2b1405bbd180520ae4284d1dedd36f9
def dec_to_bin(n):
    print(f"{n:04b}")#101101
dec_to_bin(45)