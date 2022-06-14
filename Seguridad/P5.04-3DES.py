from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
import base64
import os

mensajeOriginal = "Visita GALICIA: el paraíso".encode("utf-8")
print ("Mensaja original:", mensajeOriginal.decode("utf-8"))

while True:
  try:
    key = DES3.adjust_key_parity(get_random_bytes(24))
    break
  except ValueError:
    pass  
iv = os.urandom(8) #generamos aleatoriamente un iv

#instanciamos un nuevo objeto DES
cipher = DES3.new(key,  DES3.MODE_CFB,iv=iv)
#ciframos los datos
bytesCifrados =  cipher.encrypt(mensajeOriginal)
print ("Bytes cifrados: ", bytesCifrados)
#para imprimir una mejor representación
mensajeCifrado = base64.b64encode(bytesCifrados).decode("utf-8")
print ("Mensaje Cifrado:", mensajeCifrado)

#es necesario un nuevo objeto para descifrar
cipher = DES3.new(key, DES3.MODE_CFB,iv = iv)
#desciframos usando la misma key e iv
mensajeDescifrado = cipher.decrypt(bytesCifrados)
print ("Mensaje: ", mensajeDescifrado.decode())