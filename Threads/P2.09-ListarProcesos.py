import threading
import time

def tarea():
  time.sleep(1)
  return

for _ in range(10):
  threading.Thread(target=tarea).start()

print ("Hilos activos: ",threading.active_count())
for thread in threading.enumerate():
    print(thread.name)