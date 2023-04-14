from Crypto.PublicKey import DSA

# Creación de clave DSA
key = DSA.generate(2048)
f = open("public_key.pem", "wb")
#grabación clave pública
f.write(key.publickey().export_key())
f.close()
print ("Clave pública:\n", key.public_key().export_key())

f = open("private_key.pem", "wb")
#grabación clave privada
f.write(key.export_key())
f.close()
print ("Clave privada:\n", key.export_key())