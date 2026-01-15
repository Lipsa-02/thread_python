#program execution using main thread and sub thread
import threading
import time
def sqr(lst):
    for val in lst:
        print("{}--square({})={}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)
def cube(lst):
    for val in lst:
        print("{}---cube({})={}".format(threading.current_thread().name,val,val**3))
        time.sleep(1)
#main program
bt=time.time()
print("*"*65)
print("program execution start by:",threading.current_thread().name)
print("*"*45)
lst=[2,13,5,-16,32]
t1=threading.Thread(target=sqr,args=(lst,))
t1.name="mtroop"
t2=threading.Thread(target=cube,args=(lst,))
t2.name="Troop"
#program dispatch
t1.start()
t2.start()
print("program execution ended by:",threading.current_thread().name)
print("*"*45)
t1.join()
t2.join()
et=time.time()
print("program execution time ",(et-bt))