import threading

class miHilo(threading.Thread):
  def __init__(self, num):
    super(miHilo, self).__init__()
    self.numero = num
    self.nombre = ""
  def run(self):
    if self.nombre == "hiloPar":
      print (f'par: {self.numero}\n',end='')
    else:
      print (f'impar: {self.numero}\n',end='')

ListaHilos = [] #inicio con la lista vacía
for i in range(4):
  t = miHilo(i)
  if (i % 2) == 0:
    t.nombre = "hiloPar"
  else:
    t.nombre = "hiloImpar"    
  ListaHilos.append(t)
for h in ListaHilos:
  h.start()