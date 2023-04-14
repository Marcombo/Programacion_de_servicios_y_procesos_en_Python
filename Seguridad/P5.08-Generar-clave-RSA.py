from Crypto.PublicKey import RSA

codigoClave = "Unguessable" #conraseña
key = RSA.generate(2048)
#obtener clave privada
encrypted_key = key.export_key(passphrase=codigoClave, pkcs=8,
                              protection="scryptAndAES128-CBC")

file_out = open("rsa_key_privada.bin", "wb")
file_out.write(encrypted_key)
file_out.close()

print ("Clave privada:\n",encrypted_key)

#obtener clave pública
print("Clave pública:\n",key.publickey().export_key())

#obtener la clave pública en base a la lectura del fichero de clave privada
encoded_key = open("rsa_key_privada.bin", "rb").read()
key = RSA.import_key(encoded_key, passphrase=codigoClave)

print("Clave pública:\n",key.publickey().export_key())
print(key)