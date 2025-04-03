import time

from threading import Thread
def fib(n):
    a,b = 1,1
    for i in range(n-2):
        b,a = a+b,b

if __name__ =='__main__':
    start = time.time()
    n = int(10e5)
    a = []
    for i in range(10):
        a.append(Thread(target=fib,args=(n,)))
    for i in range(10):
        a[i].start()
    
    for i in range(10):
        a[i].join()
        print(f"{time.time() - start:.4f}")
    