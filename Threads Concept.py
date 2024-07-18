import threading
import time
Init_tim=time.time()
def cal_sq(l):
    for i in l:
        time.sleep(1)
        print(i,i**2)
l=[1,2,3,4,5]
# cal_sq(l)
t1=threading.Thread(target=cal_sq,args=(l,))
t1.start()
def cal_cub(l):
    for i in l:
        time.sleep(1)
        print(i,i**3)
# cal_cub(l)
l=[1,2,3,4,5]
t2=threading.Thread(target=cal_cub,args=(l,))
t2.start()


t1.join()
t2.join()

print("Time_Taken is",Init_tim-time.time())

