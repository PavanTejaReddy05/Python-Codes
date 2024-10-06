
def dtrs(X, Y, N):
    cs= 0
    days = 0
    while cs< N:
        days += 1
        cs+= X
        if cs>= N:
            break
        cs-= Y
    return days

# Reading input
X = int(input().strip())
Y = int(input().strip())
N = int(input().strip())

# Calculating and printing output
result = dtrs(X, Y, N)
print(result)