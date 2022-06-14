import socket

HOST = '127.0.0.1'  
PORT = 2000        

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
  s.connect((HOST, PORT))
  print('Conectado con éxito')
  s.send(b'Yo, tu cliente, te saludo.')
  #numBytes = s.send(b'Yo, tu cliente, te saludo.')
  #print (numBytes) 
  data = s.recv(1024) #línea bloqueante

print('Recibido:', repr(data))