import ipaddress

ip = ipaddress.IPv4Address('224.0.0.1')

print("Bits en la IP:", ip.max_prefixlen)
print("Multicast:", ip.is_multicast)
print("Privada:", ip.is_private)
print("Pública:", ip.is_global)
print("No es específica:", ip.is_unspecified)
print("Reservada:", ip.is_reserved)
print("Loopback:", ip.is_loopback)
print("Uso local:", ip.is_link_local)
ip1 = ip + 1
print("IP siguiente:", ip1)
ip2 = ip - 1
print("IP anterior:", ip2)
print(ip1 , "mayor que", ip2, ":", ip1 > ip2)
