n=int(input("Enter the Value: "))
for i in range (1,n+1):
    for j in  range(1,i+1):
        print("*",end=" ")
    print()
print("---------------------------")
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
print("---------------------------")


for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

print("-------------------------------")
for i in range(n):
    for j in range(n):
        if i==0 or j==n-1 or i==j:
            print("*",end="")
        else:
            print(end=" ")
    print()

print("------------------------------")

for row in range(1,n+1):                                      
    for col in range(1,n*2):
        if row==n or row+col==n+1 or col-row==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


print("------------------------------------")


for row in range(1,n+1):                                                 #for row in range(1,4):          
    for col in range(1,n*2):                                             #for col in range(1,6):                               
        if row+col==n+1 or col-row==n-1 or row==n or row*col==n*2:           #if row+col==4 or col-row==2 or row==3 or row*col==6:           
            print("*",end=" ")                                         #print("*",end=" ") 
        else:                                                          # else: 
            print(" ",end=" ")                                         # print(" ",end=" ") 
    print()                                                            #print()

print("---------------------------------------------------------")

# <<<<<<< HEAD
# #While    Method 
# '''                        *
#                          * * *
#                        *       *     
#                      *           *
#                    * * * * * * * * *'''
# =======
#While    Method 
'''                        *
                         * * *
                       *       *     
                     *           *
                   * * * * * * * * *'''
# >>>>>>> 536510fcd2b1405bbd180520ae4284d1dedd36f9
print(("While Loop"))
row=0
while row<n:
    star=row+1
    while star>0:
        print("*",end=" ")
        star=star-1
    row=row+1
    print()

print("---------------------------------------")


for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()

print("------------------------------------")


for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()



# <<<<<<< HEAD
# ''' OUTPUT
# * * * * * 
#   * * * * 
#     * * * 
#       * * 
#         *                   '''
# =======
''' OUTPUT
* * * * * 
  * * * * 
    * * * 
      * * 
        *                   '''
# >>>>>>> 536510fcd2b1405bbd180520ae4284d1dedd36f9

print("-------------------------------------")

for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
# <<<<<<< HEAD
# '''OUTPUT:-
#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * *                   '''
# =======
'''OUTPUT:-
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * *                   '''
# >>>>>>> 536510fcd2b1405bbd180520ae4284d1dedd36f9

print("-----------------------------------------")


for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()

# <<<<<<< HEAD
# '''OUTPUT:-
#  * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 
# '''
# =======
'''OUTPUT:-
 * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
'''
# >>>>>>> 536510fcd2b1405bbd180520ae4284d1dedd36f9

print("----------------------------------------------------")


for i in range(n+1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n+1):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
# <<<<<<< HEAD
# '''OUTPUT:-

#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
# * * * * * * * * * * * 
#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * *
#           *
# '''
print("----------------------------------------------------")

# |||||Star Pattern without using LOOPS|||||
def pattern(n):
    if n==0:
        return
    else:
        pattern(n-1)
        print("* "*n)

pattern(n)
# Output:-
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# =======
'''OUTPUT:-

          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * *
          *
'''
# >>>>>>> 536510fcd2b1405bbd180520ae4284d1dedd36f9
