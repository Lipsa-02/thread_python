#internal flow of threading
import threading
def welcm():
    print("Welcm() executed by :",threading.current_thread().name)
def hello():
    print("hello() executed by:",threading.current_thread().name)
def hi():
    print("hi() executed by:",threading.current_thread().name)
#main program
print("program executionstarted by :",threading.current_thread().name)
welcm()
print("line-12")
hello()
print("line-14")
hi()
print("thread execution ended by :",threading.current_thread().name)