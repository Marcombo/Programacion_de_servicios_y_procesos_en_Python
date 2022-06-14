from threading import Lock, Thread
import time

def suma_uno():
  global g
  a = g
  time.sleep(0.001)
  g = a+1

def suma_tres():
  global g
  a = g
  time.sleep(0.001)
  g =a+3     

g = 0
threads = []
for func in [suma_uno,suma_tres]:
  threads.append(Thread(target=func))
  threads[-1].start()

for thread in threads:
  thread.join()

print(g)
