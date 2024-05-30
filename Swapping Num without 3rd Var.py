A_Value=int(input("Enter A value: "))#5
B_Value=int(input("Enter B value: "))#10

#Method One
'''temp=A_Value
A_Value=B_Value
B_Value=temp'''

#Method Two
A_Value=A_Value+B_Value
B_Value=A_Value-B_Value
A_Value=A_Value-B_Value
print("now \nA value is",A_Value)
print("B value is",B_Value)