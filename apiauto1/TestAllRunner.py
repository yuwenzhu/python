import threading
from apiauto1.TestAllCase import *

def threads():
    threads=[]
    threads.append(threading.Thread(target=demo1))
    threads.append(threading.Thread(target=demo2))
    # threads.append(threading.Thread(target=demo3))
    for th in threads:
        th.start()
    th.join()

# threads()