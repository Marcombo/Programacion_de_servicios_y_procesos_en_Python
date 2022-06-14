import subprocess 

p1 = subprocess.Popen('dir', shell=True, stdin=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
  line = p1.stdout.readline()
  if not line:
    break
  #the real code does filtering here
  print (line.rstrip())
