import socket
import random

IP = ''
PORT = 2000
adivinar = random.randrange(1,9)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.bind((IP,PORT))
  s.listen()
  print("Servidor escuchando")
  print("Número a adivinar: " +str(adivinar))

  (cli,add) = s.accept() 
  print("Cliente conectado en:",add)     
  
  cli.send(b"Intenta adivinar mi numero! ")
  while True :
    data = cli.recv(64).decode()  
    print (data)
    if int(data) == adivinar:   
      cli.send(b"HAS ACERTADO") 
      break
    elif int(data) > adivinar:
      cli.send(b"Mi numero es menor ") 
    else:         
      cli.send(b"Mi numero es mayor")   
  cli.close()  