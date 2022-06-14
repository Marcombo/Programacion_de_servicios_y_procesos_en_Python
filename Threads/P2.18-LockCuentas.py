
import threading
import time
 
class CuentaBancaria:
  def __init__(self, nombre, saldo):
    self.nombre = nombre
    self.saldo = saldo
 
  def __str__(self):
    return self.nombre+' '+str(self.saldo)
 
class BankTransferThread(threading.Thread):
  def __init__(self, ordenante, receptor, cantidad):
    threading.Thread.__init__(self)
    self.ordenante = ordenante
    self.receptor = receptor
    self.cantidad = cantidad
   
  def run(self):
    lock.acquire()
     
    saldo_ordenante= self.ordenante.saldo
    saldo_ordenante-= self.cantidad
    # retraso para permitir ejecutar saltar entre hilos
    time.sleep(0.001)
    self.ordenante.saldo = saldo_ordenante
     
    saldo_receptor = self.receptor.saldo
    saldo_receptor += self.cantidad
    # retraso para permitir ejecutar saltar entre hilos
    time.sleep(0.001)
    self.receptor.saldo = saldo_receptor
     
    lock.release()
     

# Las cuentas son recursos compartidos
cuenta1 = CuentaBancaria("cuentaOrigen", 100)
cuenta2 = CuentaBancaria("cuentaDestino", 0)

lock = threading.Lock()
threads = []

for i in range(100):
  threads.append(BankTransferThread(cuenta1, cuenta2, 1))

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

print(cuenta1)
print(cuenta2)