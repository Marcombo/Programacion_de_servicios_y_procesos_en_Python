import threading
from time import time

def f_hilo(lock):
  global x
  for _ in range(1000000):
    #lock.acquire()
    for _ in range(100):
      a=x
    x=a+1    
    #lock.release()

x = 0
#tiempo_inicial = time()
lock = threading.Lock()

t1 = threading.Thread(target=f_hilo, args=(lock,))
t2 = threading.Thread(target=f_hilo, args=(lock,))

t1.start()
t2.start()

t1.join()
t2.join()

#print (time()-tiempo_inicial)
print (x)
