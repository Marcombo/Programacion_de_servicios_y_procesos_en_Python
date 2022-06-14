from encodings import utf_8
import socket
import threading

class Jugador: 
  def __init__(self): 
    self._nick = ""
    self._addr = ""
    self._jugada= ""
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

  @nick.setter 
  def nick(self, nombre): 
    self._nick = nombre 

  @addr.setter 
  def addr(self, nombre): 
    self._addr = nombre 
    
  @jugada.setter 
  def jugada(self, nombre): 
    self._jugada = nombre 
    
  @puntos.setter 
  def puntos(self, nombre): 
    self._puntos = nombre 
      
if __name__ == '__main__':
  judador1 = Jugador()
  jugador2 = Jugador()
