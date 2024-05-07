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

