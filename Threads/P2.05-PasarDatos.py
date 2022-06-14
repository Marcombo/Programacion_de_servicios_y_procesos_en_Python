import logging
import threading
import time

def thread_Apellido(name):
  print (name + " Rodríguez")
  #print (name + " Rodríguez\n")
    
nombres = ["Julio", "Javier", "Eladio", "Jose", "Manuel"]
hilos = list()
for n in nombres:
  t = threading.Thread(target=thread_Apellido, args=(n,))
  hilos.append(t)
  t.start()