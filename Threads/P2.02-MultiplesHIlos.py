import threading

def actividad():
  print ("Escribo desde un hilo")
  return

print ("INICIO")
hilos = list()
for i in range(50):
  t = threading.Thread(target=actividad)
  hilos.append(t)
  t.start()
print ("ESCRIBO EN PRINCIPAL")
