import subprocess 

p1 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
comandos = [b"verbose\n",
            b"open test.rebex.net\n",
            b"demo\n", 
            b"password\n",  
            b"ls\n",
            b"get readme.txt\n"]

for cmd in comandos:
  p1.stdin.write (cmd)
  
respuesta = p1.communicate(timeout=5)[0]
print (respuesta.decode("cp850", "ignore"))
