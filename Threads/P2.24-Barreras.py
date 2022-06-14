import time
import random
import threading

def f():
    time.sleep(random.randint(1,10))
    print("{} despertado: {}".format(threading.current_thread().name, time.ctime()))
    barrera.wait()
    print("{} pasó la barrera: {}\n".format(threading.current_thread().name, time.ctime()))

barrera = threading.Barrier(5)
for _ in range(5):
    t = threading.Thread(target=f)
    t.start()