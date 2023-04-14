alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
alfabetoCifrado = 'KLMNÑOPQRSTUVWXYZ0123456789ABCDEFGHIJ'

def cifrarCesar(men):
  mensajeCifrado= ""
  men = men.upper()
  for caracter in men:
      if caracter in alfabeto:
          index = alfabeto.index(caracter)
          mensajeCifrado += alfabetoCifrado[index]
      else: #si el carácter no existeen el alfabeto
          mensajeCifrado += caracter
  return mensajeCifrado

def descifrarCesar (menCif):
  mensajeDescifrado= ""
  for caracter in menCif:
      if caracter in alfabeto:
          index = alfabetoCifrado.index(caracter)
          mensajeDescifrado +=  alfabeto[index]
      else: #si el carácter no existeen el alfabeto
          mensajeDescifrado +=  caracter
  return (mensajeDescifrado)

print (cifrarCesar('En un lugar de la Mancha, vivía!'))
print (descifrarCesar('ÑW 4W U4PK1 NÑ UK VKWMQK, 5R5ÍK!'))

assert (cifrarCesar("I love you!")=="R UY5Ñ 8Y4!")