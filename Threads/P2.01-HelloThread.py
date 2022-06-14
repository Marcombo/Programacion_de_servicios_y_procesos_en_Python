import threading

#método al que se va a aosciar el hilo
def Saludo():
  print ('hola')

t = threading.Thread(target=Saludo)
t.start()    
print ("hola") #impresión en el hilo principal