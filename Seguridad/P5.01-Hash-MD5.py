  
import hashlib
  
#hash com md5 de un texto
Texto = "Texto de prueba".encode("utf-8")
result = hashlib.md5(Texto).hexdigest()
print("El hash de %s es: %s" % (Texto , result))

filename = input("Nombre de fichero: ")
with open(filename,"rb") as f:
  bytes = f.read() # read file as bytes
  readable_hash = hashlib.md5(bytes).hexdigest();
  print("El hash del fichero: %s es:\n%s" % (filename , readable_hash))