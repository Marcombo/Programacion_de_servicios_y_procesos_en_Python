import socket
import threading
import time

class Jugador: 
  def __init__(self): 
    self._nick = "" #nombre del jugador
    self._addr = "" #dirección del cliente
    self._jugada= "" #piedra/papel/tijera
    self._puntos= 0    
  
  @property
  def nick(self): 
    return self._nick

  @property
  def addr(self): 
    return self._addr   

  @property
  def jugada(self): 
    return self._jugada   
     
  @property
  def puntos(self): 
    return self._puntos  
  
  @property
  def libre(self): 
    if self._nick == "":
      return True
    else:
      return False     

  @property
  def sinJugar(self): 
    if self._jugada == "":
      return True
    else:
      return False 
       
  @nick.setter 
  def nick(self, nombre): 
    self._nick = nombre 

  @addr.setter 
  def addr(self, nombre): 
    self._addr = nombre 
    
  @jugada.setter 
  def jugada(self, nombre):
    if nombre in ["piedra","papel","tijera",""]:
      self._jugada = nombre 
    
  @puntos.setter 
  def puntos(self, nombre): 
    self._puntos = nombre  
    
  def puntuar(self): 
    print (self._puntos)
    self._puntos += 1    
  
  def arbitrar(self,otroJugador):
    #devuelve 0 si empate, -1 si gana otroJugador, 1 si gana el objeto actual
    if ((self.jugada =="piedra" and otroJugador.jugada =="tijera") or
              (self.jugada =="tijera" and otroJugador.jugada =="papel") or
              (self.jugada =="papel" and otroJugador.jugada =="piedra")):
      return 1
    elif ((otroJugador.jugada =="piedra" and self.jugada =="tijera") or
              (otroJugador.jugada =="tijera" and self.jugada =="papel") or
              (otroJugador.jugada =="papel" and self.jugada =="piedra")):                 
      return -1         
    else:
      return 0
            
class ManejoCliente(threading.Thread):
  def __init__(self,clientAddress,clientsocket):
    threading.Thread.__init__(self)
    self.csocket = clientsocket
    self.cAddress = clientAddress
    print ("Cliente conectado desde: ", self.cAddress)
    
  def run(self):
    print ("Escuchando a peticiones de cliente: ", self.cAddress)
    #mensaje de bienvenida con el protocolo
    bienvenida ="#INSCRIBIR#nombre#\n#JUGADA#{piedra|papel|tijera}#\n#PUNTUACION#"
    self.csocket.send(bytes(bienvenida,'UTF-8'))  
    
    while True:
      data = self.csocket.recv(512).decode("utf_8")
      print ("Enviado desde cliente:<",data,">")      
      subdatos =  data.split("#")
      respuesta="#OK#"
      if subdatos[1] == "INSCRIBIR":
        if jugador1.libre:
          jugador1.nick = subdatos[2]
          jugador1.addr = self.cAddress
        elif jugador2.libre:
          jugador2.nick = subdatos[2]
          jugador2.addr = self.cAddress
        else:
          respuesta="#NOK#ya hay dos jugadores#"
      elif subdatos[1] == "JUGADA":
        #comprobra valor válido
        if subdatos[2] not in ["piedra","papel","tijera"]:
          respuesta="#NOK#valores válidos: piedra/papel/tijera#"
        #comprobar autenticidad IP+puerto registrados
        elif self.cAddress in [jugador1.addr, jugador2.addr]:
          #estamos con el jugador 1
          if self.cAddress == jugador1.addr:
            jugador1.jugada = subdatos[2]
            #pausar hasta que jugador 2 no haga su jugada
            while (jugador2.sinJugar):
              time.sleep(0.1)
          #estamos con el jugador 2
          else:
            jugador2.jugada = subdatos[2]
            #pausar hasta que jugador 1 no haga su jugada
            while (jugador1.sinJugar):
              print (jugador1.sinJugar)
              time.sleep(0.1)
          #gana el 1
          if jugador1.arbitrar(jugador2)>0:
            jugador1.puntuar()
            respuesta="#OK#GANADOR:" + jugador1.nick + "#"
          #gana el 2
          elif jugador1.arbitrar(jugador2)<0:                 
            jugador2.puntuar()
            respuesta="#OK#GANADOR:" + jugador2.nick + "#"           
          else:
            respuesta ="#OK#EMPATE#"  
          #pequeña trampilla para que no colapsen los hilos
          time.sleep(0.5)
          jugador1.jugada =""
          jugador2.jugada =""        
        #la ip+puerto del jugador no estaba en la partida  
        else:
          respuesta="#NOK#el jugador no está en la partida#"        
      elif subdatos[1] == "PUNTUACION":
        respuesta="#OK#" + jugador1.nick + ":" + str(jugador1.puntos) + "#" + jugador2.nick + ":" + str(jugador2.puntos) + "#"

      self.csocket.send(bytes(respuesta,'UTF-8'))  
      
if __name__ == '__main__':
  jugador1 = Jugador()
  jugador2 = Jugador()
  HOST = ""
  PORT = 2000
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((HOST, PORT))
  print("Servidor iniciado. Esperando clientes...")
  while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    t = ManejoCliente(clientAddress, clientsock)
    t.start()