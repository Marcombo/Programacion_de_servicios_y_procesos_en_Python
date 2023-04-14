from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(32) # Use a stored / generated key
MensajeOriginal = 'Pureba de encriptación con AES+key+iv' # This is your data
print ("Mensaje original: ", MensajeOriginal)

#Convertir un string a un objeto de bytes codificado UNICODE
data = MensajeOriginal.encode('utf-8')

# Encriptación
cipher_encrypt = AES.new(key, AES.MODE_CFB)
BytesEncriptados = cipher_encrypt.encrypt(data)

# Nuestro datos y vector de inicialización
iv = cipher_encrypt.iv
MensajeEncriptado = BytesEncriptados
print ("Mensaje encriptado: ", MensajeEncriptado)
print ("Vector de inicialización: ", iv)


# Desencriptación
cipher_decrypt = AES.new(key, AES.MODE_CFB, iv=iv)
BytesDesncriptados = cipher_decrypt.decrypt(MensajeEncriptado)

# Conversión de bytes a string
MensajeDesencriptado = BytesDesncriptados.decode('utf-8')
print ("Mensaje desencriptado: ", MensajeDesencriptado)

#probamos coindidencia original-encriptado-desencriptado
assert MensajeOriginal == MensajeDesencriptado, 'El mensaje original no coincide con la encrptación-desencriptación'

#https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/