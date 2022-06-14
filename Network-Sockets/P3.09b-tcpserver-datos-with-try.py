from audioop import add
import socket

HOST = ''  # todas las interfaces locales a la escuchat
PORT = 2000        # Puerto de escucha

try: 
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() #línea bloqueante
    with conn:
      print(f"Conexión exitosa con el cliente. IP ({addr[0]}) Puerto ({addr[1]})")
      while True:
        data = conn.recv(1024) #línea bloqueante
        print (data)
        if data==b"0":
          break
        conn.sendall(b"mensaje recibido")

except socket.error as e: 
  print ("Error en socket: %s" % e) 
        