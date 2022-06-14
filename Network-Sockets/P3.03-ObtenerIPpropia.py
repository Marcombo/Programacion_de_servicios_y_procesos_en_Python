import socket

host = socket.gethostname()
ip = socket.gethostbyname(host)
print ("Nombre del equipo: %s" %host)
print ("Dirección IP: %s" %ip)