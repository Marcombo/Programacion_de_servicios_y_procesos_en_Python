import subprocess

def iniciaPrograma():
  try:
    SW_SHOWMAXIMIZED = 3
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW 
    info.wShowWindow = SW_SHOWMAXIMIZED
    subprocess.Popen('Notepad.exe', startupinfo=info)    
  except subprocess.CalledProcessError as e:
    print(e.output)
iniciaPrograma()
input("Pulsa una tecla para terminar la ejecución")

