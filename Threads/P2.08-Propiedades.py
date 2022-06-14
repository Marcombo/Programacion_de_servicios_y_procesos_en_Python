import threading

def Funcion_hilo():
  if (threading.current_thread().name == "miHilo7"):
    threading.current_thread().name = "nombre-cambiado"
  print (f"Hola desde: {threading.current_thread().name} \
  ID {threading.current_thread().ident}\n", end="")
  #threading.current_thread().ident = 666 #comprobaicón error
    
hilos = list()
for n in range(1,11):
  t = threading.Thread(target=Funcion_hilo, name = "miHilo")
  if (n>5):
    t.name = "miHilo"+str (n)
  hilos.append(t)
  t.start()