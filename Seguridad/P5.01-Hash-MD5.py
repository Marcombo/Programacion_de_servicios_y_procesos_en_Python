import hashlib
  
#hash co md5 de un texto
Texto = "Texto de prueba".encode("utf-8")
HashCode= hashlib.md5(Texto).hexdigest()
print("El hash de %s es: %s" % (Texto , HashCode))

#hash con md5 de un fichero
filename = input("Nombre de fichero: ")
with open(filename,"rb") as f:
  bytes = f.read()
  HashCode = hashlib.md5(bytes).hexdigest();
  print("El hash del fichero: %s es:\n%s" % (filename ,HashCode))