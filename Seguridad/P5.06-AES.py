from Crypto.Cipher import AES

mensajeOriginal = b"Hola, algoritmo AES"
key = b'Clave de 16 Byte'
print ("Original: ", mensajeOriginal)

#cifrar
cipher = AES.new(key, AES.MODE_EAX) #sin iv
mensajeCifrado, tag = cipher.encrypt_and_digest(mensajeOriginal)
print ("Cifrado: ", mensajeCifrado)

#descifrar
cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
mensajeDescifrado = cipher.decrypt(mensajeCifrado)
try:
  cipher.verify(tag)
  print("Descifrado: ", mensajeDescifrado)
except ValueError:
  print("Clave incorrecta o mensaje corrupto")

assert (mensajeDescifrado == mensajeDescifrado)