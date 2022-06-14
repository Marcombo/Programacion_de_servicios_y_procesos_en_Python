
import threading

def ping(cond):
  for _ in range(20):
    with cond:
      cond.wait()
      print ("ping")
      cond.notify()

def pong(cond):
  for _ in range(20):
    with cond:
      cond.wait()
      print ("pong")
      cond.notify()

cond = threading.Condition()

t1= threading.Thread(target=ping, args=(cond,))
t2=threading.Thread(target=pong, args=(cond,))
t1.start()
t2.start()
with cond:
  cond.notify()