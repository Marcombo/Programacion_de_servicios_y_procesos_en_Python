import socket

HOST = '127.0.0.1'  
PORT = 2000        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.connect((HOST, PORT))
  print('Conectado con éxito')
except socket.error as exc:
  print ("Excepción de socket: %s" % exc)
finally:
  #cerramos la conexión, aunque el servidor ya la habrá cerrado
  s.close()