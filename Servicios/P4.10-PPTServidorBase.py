from encodings import utf_8
import socket
import threading

class ManejoCliente(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        msg = ''
        while True:
            data = self.csocket.recv(512).decode('UTF-8')
            if data=='bye':
              break
            print ("from client", data)
            self.csocket.send(bytes(data,'UTF-8'))
        print ("Client at ", clientAddress , " disconnected...")   
        
if __name__ == '__main__':
  HOST = ""
  PORT = 2000
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((HOST, PORT))
  print("Server started")
  print("Waiting for client request..")
  while True:
      server.listen(1)
      clientsock, clientAddress = server.accept()
      t = ManejoCliente(clientAddress, clientsock)
      t.start()