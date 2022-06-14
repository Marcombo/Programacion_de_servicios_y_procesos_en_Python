import psutil

for proc in psutil.process_iter():
  try:
    # Obtener el nombre del proceso
    nombreProceso = proc.name()    
    if proc.name() == "notepad.exe":
      PID = proc.pid
      print("Eliminando el proceso: ", nombreProceso , ' ::: ', PID)
      proc.kill()    
  except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    print ("error")

