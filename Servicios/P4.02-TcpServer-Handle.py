import socketserver

class TCPSocketHandler(socketserver.BaseRequestHandler):
  #Clase para manejar las conexiones, se instancia una por cliente

  def handle(self):
    #medodo a sobreescribir para nuestro propio manejo
    #self.request se refiere al socket client conectado
    print (f"Se han conectado desde: {self.client_address[0]} [{self.client_address[1]}]")

    self.data = self.request.recv(128).strip()
    print("Datos recibidos: ", self.data)
    #remitimos los mismos datos en mayúscula
    self.request.sendall(self.data.upper())
    # if self.data == b"0":
    #   break
    # if self.data ==b"#":
    #   raise KeyboardInterrupt

if __name__ == "__main__":  
  HOST, PORT = "", 2000

  # instanciamos el socket servidor con la clase asociada de callback
  server = socketserver.TCPServer((HOST, PORT), TCPSocketHandler)

  # activamos el servidor (ponemos a la espera de clientes)
  # podemos provocar una excepción con Ctrl-C
  try:
    while True:
      server.handle_request() 
  except KeyboardInterrupt:
    print ("servidor finalizado")
    