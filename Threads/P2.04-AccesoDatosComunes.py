import threading
import time
import random

def tareaUno():
  global Realizado
  #time.sleep (random.random())
  if not Realizado:
    print("Tarea realizada")  
    Realizado = True    
  return

Realizado = False
t = threading.Thread(target=tareaUno)
t.start()
tareaUno()
time.sleep(1)
