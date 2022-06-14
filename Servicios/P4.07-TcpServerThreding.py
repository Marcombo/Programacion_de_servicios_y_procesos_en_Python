import threading
import socketserver

class ThreadedTCPRequestHandler(socketserver.StreamRequestHandler):

  def handle(self):
    data = self.rfile.readline().strip().decode('ascii')
    #data = str(self.request.recv(1024), 'ascii')
    cur_thread = threading.currentThread()
    print (threading.current_thread().name)
    response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
    self.request.sendall(response)

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
  pass


if __name__ == "__main__":
  HOST, PORT = "", 2000
  server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)

  # activamos el servidor (ponemos a la escucha)
  # podomos porvocar una excepción con Ctrl-C
  try:
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    while True:
      pass
  except KeyboardInterrupt:
    print ("servidor finalizado")    
    