import socketserver

class TCPStreamHandler(socketserver.StreamRequestHandler):
  #Clase para manejar las conexiones, se instancia una por cliente
  #transmisión de datos por stream
 
  def handle(self):
    # self.rfile es un stream de lectura
    # self.wfile es un stream de escritura
    print (f"Se han conectado desde: {self.client_address[0]} [{self.client_address[1]}]")
    while True:
      self.data = self.rfile.readline().strip()
      print("Datos recibidos: ", self.data)
      #remitimos los mismos datos en mayúscula
      self.wfile.write(self.data.upper())
      #self.wfile.writelines((b"uno", b"dos",b"tres"))
      if self.data == b"":
        break
      if self.data ==b"#":
        raise KeyboardInterrupt
        


if __name__ == "__main__":  
  HOST, PORT = "", 2000

  # instanciamos el socket servidor con la clase asociada de callback
  server = socketserver.TCPServer((HOST, PORT), TCPStreamHandler)
 
  # activamos el servidor (ponemos a la escucha)
  # podomos porvocar una excepción con Ctrl-C
  try:
    server.serve_forever()
  except KeyboardInterrupt:
    print ("servidor finalizado")
    


