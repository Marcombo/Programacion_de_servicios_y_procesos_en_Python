from threading import *
import time

def hilo():				
  for i in range(10):
    print('Hilo no Daemon (Backgoround)')
    time.sleep(1)

t = Thread(target=hilo)
t.daemon = True
t.start()	

time.sleep(5)				
print('Hilo principal')