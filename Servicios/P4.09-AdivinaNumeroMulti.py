import socket
import random
import threading

adivinar = random.randrange(1,9)

def ManejaCliente(c,a):
  c.send(b"Intenta adivinar mi numero! ")
  while True :
    data = c.recv(64).decode()  
    print (data)
    if int(data) == adivinar:   
      c.send(b"HAS ACERTADO") 
      break
    elif int(data) > adivinar:
      c.send(b"Mi numero es menor ") 
    else:         
      c.send(b"Mi numero es mayor")   
  c.close() 


if __name__ == '__main__':
  IP = ''
  PORT = 2000
  
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((IP,PORT))
    s.listen()
    print("Servidor escuchando")
    print("Número a adivinar: " +str(adivinar))
   
    while True:
      (cli,addr) = s.accept() 
      print("Cliente conectado en:",addr)       
      #con cada conexión iniciamos un nuevo hilo que lo atienda
      t = threading.Thread(target=ManejaCliente, args=(cli,addr))
      t.start()