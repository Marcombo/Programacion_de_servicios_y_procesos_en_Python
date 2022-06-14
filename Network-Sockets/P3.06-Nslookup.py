import socket 

ip = "216.58.209.69"
try:
  dominio = socket.gethostbyaddr(ip)[0]
  print ("La IP %s tiene una entrada DNS: %s" %(ip, dominio))
except socket.error as msg:
  print ("%s: %s" %(ip, msg))