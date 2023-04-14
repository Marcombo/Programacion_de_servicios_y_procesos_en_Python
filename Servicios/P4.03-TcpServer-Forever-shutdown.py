from asyncio.windows_events import NULL
import socketserver
import time
import threading

class TCPSocketHandler(socketserver.BaseRequestHandler):
  #Clase para manejar las conexiones, se instancia una por cliente
 # def __init__(self, server_address, RequestHandlerClass, ):    
   
  def set_shutdown_request(self):
    self.shutdown_request = True


  def handle(self):
    #medodo a sobreescribir para nuestro propio manejo
    #self.request se refiere al socket client conectado
    print (f"Se han conectado desde: {self.client_address[0]} [{self.client_address[1]}]")
    #print (self.server.request_queue_size)
    self.shutdown_request = False
    while not self.shutdown_request:
      print (self.shutdown_request)
      self.data = self.request.recv(128).strip()
      print("Datos recibidos: ", self.data)
      #remitimos los mismos datos en mayúscula
      self.request.sendall(self.data.upper())
      if self.data == b"0":
        break
      if self.data ==b"#":
        raise KeyboardInterrupt

def Servir(servidor):


  # instanciamos el socket servidor con la clase asociada de callback
  servidor = socketserver.TCPServer((HOST, PORT), TCPSocketHandler)
  # activamos el servidor (ponemos a la escucha)
  # podomos porvocar una excepción con Ctrl-C
  try:
    servidor.serve_forever()
  except KeyboardInterrupt:
    print ("servidor finalizado")
  
if __name__ == "__main__":  
  HOST, PORT = "", 2000
   # instanciamos el socket servidor con la clase asociada de callback
  server = socketserver.TCPServer((HOST, PORT), TCPSocketHandler)      
  server_thread = threading.Thread(target=server.serve_forever)
  # Exit the server thread when the main thread terminates
  server_thread.daemon = True
  server_thread.start()
    
  print ("uno") 
  time.sleep(10)
  print ("dos")
  server.
  server.shutdown()
  print ("tres")
  
 