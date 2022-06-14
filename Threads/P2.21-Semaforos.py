import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
          format='(%(threadName)-9s) %(message)s',)

class ThreadPool(object):
  def __init__(self):
    super(ThreadPool, self).__init__()
    self.active = []
    self.lock = threading.Lock()
  def makeActive(self, name):
    with self.lock:
      self.active.append(name)
      logging.debug('Running: %s', self.active)
  def makeInactive(self, name):
    with self.lock:
      self.active.remove(name)
      logging.debug('Running: %s', self.active)

def f(s, pool):
  logging.debug('Esperando para unirse al grupo')
  with s:
    name = threading.current_thread().name
    pool.makeActive(name)
    time.sleep(0.5)
    pool.makeInactive(name)


pool = ThreadPool()
s = threading.Semaphore(3)
for i in range(10):
  t = threading.Thread(target=f, name='thread_'+str(i), args=(s, pool))
  t.start()