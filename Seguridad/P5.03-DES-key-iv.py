from Crypto.Cipher import DES
import base64
import os

mensajeOriginal = "Visita GALICIA: el paraíso".encode("utf-8")
print ("Mensaja original:", mensajeOriginal.decode("utf-8"))

key = b"abc123.." #establecemos una clave
iv = os.urandom(8) #generamos aleatoriamente un iv

#instanciamos un nuevo objeto DES
cipher = DES.new(key,  DES.MODE_OFB,iv=iv)
#ciframos los datos
bytesCifrados =  cipher.encrypt(mensajeOriginal)
print ("Bytes cifrados: ", bytesCifrados)
#para imprimir una mejor representación
mensajeCifrado = base64.b64encode(bytesCifrados).decode("utf-8")
print ("Mensaje Cifrado:", mensajeCifrado)

#es necesario un nuevo objeto para descifrar
cipher = DES.new(key, DES.MODE_OFB,iv = iv)
#desciframos usando la misma key e iv
mensajeDescifrado = cipher.decrypt(bytesCifrados)
print ("Mensaje: ", mensajeDescifrado.decode())
