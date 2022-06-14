import threading
import time

class HiloAbortable(threading.Thread):
   
  def __init__(self):
    super(HiloAbortable, self).__init__()
    self._abort_event = threading.Event()

  def abort(self):
    self._abort_event.set()

  def aborted(self):
    return self._abort_event.is_set()
  
  def run(self):    
    while (True):
      if (self.aborted()):
        print ("Hilo abortado")
        break
      #resto del trabajo a ejecutar
      print ("trabajando...")
      
h =HiloAbortable()
h.start()
time.sleep(1)
print ("Antes de invocación a abort()")
h.abort()
print ("Después de invocación de abort()")

  
  
