import socketserver

class UDPHandler(socketserver.BaseRequestHandler):
  #self.request es el par [datos,socketServidor]

  def handle(self):
    data = self.request[0].strip()
    sock = self.request[1]
    print(" El cliente: {} envió:".format(self.client_address[0]))
    print(data)
    #bajo alguna circunstancia podemos detener el servidor con la siguiente línea    
    if data ==b"#":
      raise KeyboardInterrupt
    #envío de datos al cliente
    sock.sendto(data.upper(), self.client_address)

if __name__ == "__main__":
  HOST, PORT = "", 2000
  with socketserver.UDPServer((HOST, PORT), UDPHandler) as server:
    # activamos el servidor (ponemos a la escucha)
    # podomos porvocar una excepción con Ctrl-C
    try:
      server.serve_forever()
    except KeyboardInterrupt:
      print ("servidor finalizado")
    