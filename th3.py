#internalflow with main thread and sub threads
import threading
def welcm():
    print("Welcm() executed by :",threading.current_thread().name)
def hello():
    print("hello() executed by:",threading.current_thread().name)
def hi():
    print("hi() executed by:",threading.current_thread().name)
#main program
print("*"*45)
print("program execution started by :",threading.current_thread().name)
print("*"*45)
t1=threading.Thread(target=welcm)
t1.name="TR"
print("line-12")
t2=threading.Thread(target=hello)
t2.name="RS"
print("line-14")
t3=threading.Thread(target=hi)
t3.name="DR"
#dispatch the sub thread to the target functions
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("thread execution ended by :",threading.current_thread().name)