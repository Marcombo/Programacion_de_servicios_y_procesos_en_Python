import socket

HOST = '127.0.0.1'  # direccion de loopback standard para localhost
PORT = 2000        # Puerto de escucha

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  s.bind((HOST, PORT))
  s.listen(1)
  conn, addr = s.accept() #función bloqueante
  print (f"Conexión exitosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
  #cerramos la conexión con ese cliente
  conn.close()   
except socket.error as exc:
  print ("Excepción de socket: %s" % exc)
finally:
  #cerramos la escucha general de nuestro servidor
  s.close()