import time
import threading
def son(x):
    print("Printing the Squares...")
    for i in x:
        time.sleep(1)
        print("i=",i,"Sqrs=",i**2)
def con(x):
    print("Printing the Cubes...")
    for i in x:
        time.sleep(1)
        print("i=",i,"Cubes=",i**3)

arr=[12,3,4,11,5]
startTime=time.time()
son(arr)
con(arr)
endTime=time.time()
print("Time Required= ",endTime-startTime,"sec")
