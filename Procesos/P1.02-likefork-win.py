from multiprocessing import Process
import os

def hijo():
   print("Padre: %d, Hijo: %d\n" % ( os.getppid(),os.getpid()))
   os._exit(0)  

def padre():
  while True:
    p = Process(target=hijo)
    p.start()
    print ("\nNuevo hijo creado " , p.pid)
    p.join()
    reply = input("Pulsa 's' si quieres crear un nuevo proceso\n")
    if reply != 's': 
      break
if __name__ == '__main__':
  padre()