#program to print 1-n numbers after each and every second by using threads.
#functional programming
import threading
import time
class blue:
    def sqr(n):
        if (n<=0):
            print("invalid input")
        else:
            print("numbers within",n)
            print("*"*45)
            for val in range(1,n+1):
                print("{}----value:{}".format(threading.current_thread().name,val))
                time.sleep(1)

#main program
n=int(input("enter how many numbers you want:"))
t1=threading.Thread(target= blue.sqr(n),args=(n,))
t1.start()