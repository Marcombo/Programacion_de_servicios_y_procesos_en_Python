import subprocess
try:
  subprocess.run(['Notepad.exe',])
  subprocess.run(['c:/windows/notepad.exe',])
  subprocess.run(['Notepad.exe','texto.txt'])
except subprocess.CalledProcessError as e:
    print(e.output)