import time

from threading import Thread
from multiprocessing import Process
def fib(n):
    a,b = 1,1
    for i in range(n-2):
        b,a = a+b,b

if __name__ =='__main__':
    n = int(10e5)
    start = time.time()
    a = []
    for i in range(10):
        a.append(Process(target=fib,args=(n,)))
    for i in range(10):
        a[i].start()
    
    for i in range(10):
        a[i].join()
        print(f"{time.time() - start:.4f}")