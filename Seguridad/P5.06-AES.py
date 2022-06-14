from Crypto.Cipher import AES

data = b"Hola, algoritmo AES"
key = b'Sixteen byte key'
#key2 = b'1234567890abcdef'
cipher = AES.new(key, AES.MODE_EAX)

textoCifrado, tag = cipher.encrypt_and_digest(data)

cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)
textoOriginal = cipher.decrypt(textoCifrado)
try:
    cipher.verify(tag)
    print("Mensaje auténtico:", textoOriginal)
except ValueError:
    print("Clave incorrecta o mensaje corrupto")