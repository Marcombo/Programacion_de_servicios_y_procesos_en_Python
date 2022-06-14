import ipaddress
import socket

direcciones = socket.getaddrinfo(socket.gethostname(), None)
for ip in direcciones:
  # ip_ver = ipaddress.ip_address(str(ip[4][0]))
  # if ip_ver.version == 4:
    print (ip[4][0])
