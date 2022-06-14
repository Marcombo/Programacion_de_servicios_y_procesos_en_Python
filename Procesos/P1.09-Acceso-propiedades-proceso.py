import psutil
import os
import subprocess
import sys

def ProcesoActual ():
  return psutil.Process(os.getpid())

def esWindows():
  try:
    sys.getwindowsversion()
  except AttributeError:
    return (False)
  else:
    return (True)

print (ProcesoActual().name())  #nombre
print (ProcesoActual().cwd()) #path de ejecución
#prioridad ante del cambio
print  (ProcesoActual().nice())
if esWindows():
  subprocess.check_output("wmic process where processid=\""+str(os.getpid())+"\" CALL   setpriority \"below normal\"") 
else:
  os.nice(1)
#prioridad después del cambio
print (ProcesoActual().nice())
a = input()