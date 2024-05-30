# '''Given  a  string,  split  it  on  whitespace,  capitalize  each  element  of  the resulting  list  
# and  join  them  back  into  a  string.
# Your  implementation should use a list comprehension.'''
# string="Hello today we are going to say about"
# l=string.split()
# for i in l:
#     print(("".join(i.capitalize())),end=" ")
lst = [2, 7, 8, 6, 5, 5, 4, 4, 8]
s = {True if n % 2 == 0 else False for n in lst}
print(s)