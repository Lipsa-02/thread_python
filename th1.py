#Default threading present in python
import threading
thname=threading.current_thread().name
thnm=threading.active_count()
print("Default thread name:",thname)
print("Default no. of threads :",thnm)