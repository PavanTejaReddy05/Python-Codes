# Read input strings
string = input()
substring = input()

# Initialize a count variable
count = 0

# Find and count occurrences of the substring
while substring in string:
    # Find the index of the next occurrence of the substring
    index = string.find(substring)
    # Increment the count
    count += 1
    # Move the search position to the character after the found occurrence
    string = string[index + 1:]

# Print the final count
print(count)
