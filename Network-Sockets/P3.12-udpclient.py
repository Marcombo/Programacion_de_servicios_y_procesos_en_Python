import socket

HOST = '127.0.0.1'  
PORT = 2000      

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
  s_addr = (HOST, PORT) 
  server_address = (s_addr)
  message = b'Saludos desde el cliente'

  # enviar
  print('Enviando {!r}'.format(message))
  sent = s.sendto(message, server_address)

  # recibir
  print('Esperando por la respuesta')
  data, server = s.recvfrom(1024) #línea bloqueante
  print('recibidos {!r}'.format(data))

