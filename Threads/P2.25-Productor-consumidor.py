import threading
import time
import logging
import random
import queue

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

class HiloProductor(threading.Thread):
  def __init__(self,name=None):
    super(HiloProductor,self).__init__()
    self.name = name

  def run(self):
    while True:
      if not q.full():
        item = random.randint(1,10)
        q.put(item)
        logging.debug('Insertando "' + str(item)  
                      + '" : ' + str(q.qsize()) + ' elementos en la cola')
        time.sleep(random.random())
    return

class HiloConsumidor(threading.Thread):
  def __init__(self,name=None):
    super(HiloConsumidor,self).__init__()
    self.name = name
    return

  def run(self):
    while True:
      if not q.empty():
        item = q.get()
        logging.debug('Sacando "' + str(item) 
                      + '" : ' + str(q.qsize()) + ' elementos en la cola')
        time.sleep(random.random())
    return

p = HiloProductor(name='productor')
p2 = HiloProductor(name='productor2')

c = HiloConsumidor(name='consumidor')

p.start()
p2.start()  
c.start()