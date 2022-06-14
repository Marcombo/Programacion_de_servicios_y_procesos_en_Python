from threading import *
import time

def hilo():
  #time.sleep(1)
  print("Hola")

T = Thread(target = hilo)
T.daemon=True
T.start()
