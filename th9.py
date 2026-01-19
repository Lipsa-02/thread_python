import threading,time
class thr:
    def value(self,n):
        for i in range(1,n+1):
            if (i%2==0):
                print("*"*30)
                print("even number is:",i)
            else:
                print("odd number is:",i)
                time.sleep(0.5)
#main program
n=int(input("Enter value for n:"))
print("showing result upto the range:",n)
t=thr()
thread=threading.Thread(target=t.value(n),args=(n,))
thread.start()
thread.join()
print("work done")