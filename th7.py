#oops programming with threading
#program toprint1-n numbers after each and evry 0.5second
import threading,time
class color:
    def __init__(self,n):
        self.n=n
    def yellow(self):
        if(self.n<=0):
            print("invalid input",self.n)
        else:
            print("Numbers within:",self.n)
            for val in range(1,self.n+1):
                print("{}---value:{}".format(threading.current_thread().name,val))
                time.sleep(0.5)

#main program
n=int(input("enter how many numbers you want to generate:"))
c=color(n)
t1=threading.Thread(target=c.yellow)
t1.start()
