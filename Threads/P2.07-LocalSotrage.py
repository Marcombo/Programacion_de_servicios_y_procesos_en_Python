import threading
import random

def mostrar(d):
  try:
    val = d.valor
  except AttributeError:
    print(f"{threading.current_thread().name}: Aún no inicializado\n", end="")
  else:
   print(f"{threading.current_thread().name}: {val}\n", end="")

def hilo(dato):
  mostrar(dato)
  dato.valor = random.randint(1, 100)
  mostrar(dato)

dato = threading.local() #variable con instancia local en cada hilo
mostrar(dato)
dato.valor = 999
mostrar(dato)

for i in range(3):
  t = threading.Thread(target=hilo, args=(dato,))
  t.start()