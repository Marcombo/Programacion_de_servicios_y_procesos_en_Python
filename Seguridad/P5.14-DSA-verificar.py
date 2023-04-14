from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import json

#abrimos un fichero JSON con el texto y la firma 
#viene codificamos en dos caracteres hexadecimales cada byte
f = open("mensajefirmado.txt", "r")
mensajeFirmado =f.read()
print (mensajeFirmado)
mensajeRecibido = json.loads(mensajeFirmado)

#creamos un verificador con la firma leida en el fichero JSON
#usamos la clave pública del remitente
f = open("public_key_firma.pem", "r")
hash_obj = SHA256.new(bytes.fromhex(mensajeRecibido["mensaje"]))
pub_key = DSA.import_key(f.read())
verificador = DSS.new(pub_key, 'fips-186-3')

# Verificar la autenticidad del mensaje recibido 
# en realidad lo hacemos del hash de todo el mensaje
try:
  verificador.verify(hash_obj, bytes.fromhex(mensajeRecibido["firma"]))
  print ("El mensaje es AUTENTICO")
except ValueError:
  print ("Este mensaje no ha sido firmado de forma válida")