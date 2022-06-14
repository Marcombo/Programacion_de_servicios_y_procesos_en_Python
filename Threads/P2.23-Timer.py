import threading
import time

def tarea(num):
  for _ in range (num):
    print("Ejecutando tarea...")
    time.sleep(1)
    #print (threading.currentThread().name)

veces = 10
t = threading.Timer(3, tarea, [veces,])
print("Iniciando hilo con temporizador")
t.start() #será ejecutado tras tres segundos
time.sleep(5)
#prueba para cancelar el hilo
print("Cancelando la tarea <<si no se ha comenzado>>")
t.cancel()