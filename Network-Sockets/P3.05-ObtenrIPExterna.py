import socket

try:
  host = 'www.amazon.es'
  #host = socket.getfqdn() 
  #host = 'DESKTOP-KEFADT0'
  print ("IP de %s: %s" %(host,socket.gethostbyname(host)))
except socket.error as msg:
  print ("%s: %s" %(host, msg))