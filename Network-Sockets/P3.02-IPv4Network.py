import ipaddress

network = ipaddress.IPv4Network("192.168.1.0/24")

print("Dirección de la red:", network.network_address)
print("Dirección de broadcast:", network.broadcast_address)
print("Máscara de red:", network.netmask)
print("Red y máscara de red:", network.with_netmask)
print("Red y máscara de host:", network.with_hostmask)
print("Longitud de la máscara de red", network.prefixlen)
print("Máximo número de equipos en la red:", network.num_addresses)
print("La red 192.168.0.0/16 la contiene:", 
  network.overlaps(ipaddress.IPv4Network("192.168.0.0/16")))
print("Supernet:", network.supernet(prefixlen_diff=1))
print("La red es una subnet de 192.168.0.0/16:",
	network.subnet_of(ipaddress.IPv4Network("192.168.0.0/16")))
print("La red es una supernet de 192.168.0.0/16:",
	network.supernet_of(ipaddress.IPv4Network("192.168.0.0/16")))
print("Comparar con 192.168.0.0/16:",
	network.compare_networks(ipaddress.IPv4Network("192.168.0.0/16")))
