from Crypto.PublicKey import RSA

key = RSA.generate(2048)
private_key = key.export_key()
file_out = open("privada_usuario_A.pem", "wb")
file_out.write(private_key)
file_out.close()

public_key = key.publickey().export_key()
file_out = open("publica_usuario_A.pem", "wb")
file_out.write(public_key)
file_out.close()