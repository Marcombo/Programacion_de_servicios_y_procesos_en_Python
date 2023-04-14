from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import json

f = open("private_key_firma.pem", "r")
key =DSA.import_key(f.read())

# Firmar un mensaje con la clave privada
mensaje = b"Comprobamos quien firma este mensaje"
hash_obj = SHA256.new(mensaje)
firmador = DSS.new(key, 'fips-186-3')
firma = firmador.sign(hash_obj)

#creamos un fichero JSON con el texto y la firma 
#lo codificamos en dos caracteres hexadecimales cada byte
mensajeFirmado = json.dumps({'mensaje':mensaje.hex(), 'firma':firma.hex()})
#print (mensajeFirmado)
f = open("mensajefirmado.txt", "w")
f.write(mensajeFirmado)
f.close()