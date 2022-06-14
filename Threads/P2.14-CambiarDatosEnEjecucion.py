from threading import Thread
import time
import logging

logging.basicConfig( level=logging.DEBUG,
    format='[%(threadName)-10s]: %(message)s')

class miHilo(Thread):
  def __init__(self):
    super(miHilo, self).__init__()
    self.nombre= ""
  def run(self):
    for i in range (20):      
      #print (self.nombre)
      logging.debug ("iteración %i, nombre: %s", i+1,self.nombre)
      time.sleep (0.1)

t = miHilo()
t.nombre ="Pepe"
t.start()
time.sleep(0.5)
#modificamos un dato posteriormente a inicializarse el hilo
t.dato ="Lola"
  