import socket

HOST, PORT = "localhost", 2000
data = "hola desde cliente udp"

#definir
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
  #se puede observar que no hay conectar
  #enviar
  sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
  #recibir
  recibido = str(sock.recv(64), "utf-8")

print("Enviado:  {}".format(data))
print("Recibido: {}".format(recibido))