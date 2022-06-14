import threading 
import logging

logging.basicConfig( level=logging.DEBUG,
    format='[%(threadName)-10s]: %(message)s')
  
def imprime_x(x, n): 
  logging.debug("INICIO")
  for i in range(n):
    logging.debug (x)
  logging.debug("FIN")
  
t1 = threading.Thread(target=imprime_x, args=("norte", 5,)) 
t2 = threading.Thread(target=imprime_x, args=("sur", 10,)) 

t1.start() 
t2.start() 
	
# espera hasta que el hilo t1 hay finalizado
t1.join() 
# espera hasta que el hilo t2 hay finalizado
t2.join() 

#llega hasta aquí cuando los dos hilos han
logging.debug("Fin!")