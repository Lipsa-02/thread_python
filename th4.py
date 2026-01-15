#internal flow of main thread with execution time
import threading
import time
def square(lst):
    for val in lst:
        print("{}---square({})={}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)
def cube(lst):
    for val in lst:
        print("{}---cube({})={}".format(threading.current_thread().name,val,val**3))
        time.sleep(1)


#main program
bt=time.time()
print("*"*56)
print("program execution start by :",threading.current_thread().name)
print("*"*45)
lst=[12,4,5,16,-6,17,19,4,13,45]
square(lst)
print("*"*45)
cube(lst)
print("*"*45)
print("program execution end by:",threading.current_thread().name)
et=time.time()
print("execution time of the program only main thread without sub threads: ",(et-bt))