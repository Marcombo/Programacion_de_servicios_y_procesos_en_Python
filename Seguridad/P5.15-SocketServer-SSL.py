import socket
import ssl

HOST ='localhost'
PORT = 4444

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert-ssl\certificado.pem', 'cert-ssl\clave-privada.key')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
  sock.bind((HOST, PORT))
  sock.listen(5)
  print (f"Servidor correiendo en: {HOST},{PORT}")
  #solapaar el socket sobre SSL
  with context.wrap_socket(sock, server_side=True) as ssock:
    while True:
      conn, addr = ssock.accept()
      print (f"Conexión desde: {addr}")
      #enviar datos
      data = "Bienvenido al servidor SSL ("+HOST+":"+str(PORT)+")"
      conn.sendall (data.encode("utf-8"))
      #recibir datos
      data =conn.recv()
      print (data)