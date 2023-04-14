import socket
import ssl

HOST = 'localhost'
PORT = 4444

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert-ssl\certificado.pem')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
  #solapaar el socket sobre SSL
  with context.wrap_socket(sock, server_hostname=HOST) as ssock:
    print(ssock.version())
    ssock.connect((HOST, PORT))
    print ("Conexión con éxito")
    #recibir datos
    data = ssock.recv(1024)
    print(f"Recibido: {data!r}")
    #enviar datos
    ssock.sendall("hola, soy un cliente SSL".encode("utf-8"))