from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

data = "La criptografía a través en Python a través de <<pycryptodome>> es consistente".encode("utf-8")
file_out = open("Datos_Encriptados.bin", "wb")

recipient_key = RSA.import_key(open("publica_usuario_A.pem").read())
session_key = get_random_bytes(16)

# Encriptar la sesión con la clave pública del usuario_A
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_session_key = cipher_rsa.encrypt(session_key)

# Encriptar los datos con la sesión de AES
cipher_aes = AES.new(session_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(data)
[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
file_out.close()