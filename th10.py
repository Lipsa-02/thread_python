 #deadlock remove/ lock method
import threading,time
L=threading.Lock()
def bowl(n):
  #get the lock
 L.acquire()
 try:
        if n <= 0:
            print("invalid input")
        else:
          print("{}-->mul table for {}".format(threading.current_thread().name,n))
          print("*"*35)
          for i in range(1,11):
            print("{}----{} x {}={}".format(threading.current_thread().name,n,i,n*i))
            time.sleep(0.5)
 finally:
  L.release()
#main program
#sub threads
t1=threading.Thread(target=bowl,args=(15,))
t2=threading.Thread(target=bowl,args=(13,))
t3=threading.Thread(target=bowl,args=(19,))
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("work done")