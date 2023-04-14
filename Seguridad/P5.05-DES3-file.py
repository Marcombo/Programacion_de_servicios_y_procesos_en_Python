from Crypto.Cipher import DES3
from hashlib import md5

def encriptar (fileOrigen, fileDestino, key):
  cipher = DES3.new(key, DES3.MODE_EAX, nonce=b'0')
  with open(fileOrigen, 'rb') as input_file:
    file_bytes = input_file.read()
    enc_file_bytes = cipher.encrypt(file_bytes)

  with open(fileDestino, 'wb') as output_file:
    output_file.write(enc_file_bytes)

def desencriptar (fileOrigen, fileDestino, key):
  cipher = DES3.new(key, DES3.MODE_EAX, nonce=b'0')
  with open(fileOrigen, 'rb') as input_file:
    file_bytes = input_file.read()
    dec_file_bytes = cipher.decrypt(file_bytes)

  with open(fileDestino, 'wb') as output_file:
    output_file.write(dec_file_bytes)
      

key = "abc123."

key_hash = md5(key.encode('ascii')).digest() # 16-byte key
tdes_key = DES3.adjust_key_parity(key_hash)

encriptar("textoPlano.txt","textoEncriptado.txt",tdes_key)
desencriptar("textoEncriptado.txt", "textoDesencriptado.txt",tdes_key)