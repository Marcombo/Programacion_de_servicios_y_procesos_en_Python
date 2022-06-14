from threading import Lock, Thread
import time

def suma_uno():
  global g
  lock.acquire()
  a = g
  time.sleep(0.001)
  g = a+1
  lock.release()

def suma_tres():
  global g
  with lock: 
    a = g
    time.sleep(0.001)
    g =a+3     

lock = Lock()
g = 0
threads = []

for func in [suma_uno,suma_tres]:
  threads.append(Thread(target=func))
  threads[-1].start()

for thread in threads:
  thread.join()

print(g)
