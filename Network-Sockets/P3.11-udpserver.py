import socket

HOST = ''  
PORT = 2000        

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

  s_addr = (HOST, PORT)
  s.bind(s_addr)
  #recibir
  datos, addr = s.recvfrom(1024) #línea bloqueante
  print('recibidos  {} bytes de {}'.format(len(datos), addr))
  print(datos)

  #enviar
  if datos:
    sent = s.sendto(b"Saludos desde el Servidor UDP", addr)
    print('enviados {} bytes de vuelta a {}'.format(sent, addr))
