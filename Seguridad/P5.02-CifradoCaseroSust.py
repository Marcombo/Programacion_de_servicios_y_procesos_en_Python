alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
alfabetoCifrado = 'KLMNÑOPQRSTUVWXYZ0123456789ABCDEFGHIJ'

def cifrar(men):
  mensajeCifrado= ""
  men = men.upper()
  for caracter in men:
      if caracter in alfabeto:
          index = alfabeto.index(caracter)
          mensajeCifrado += alfabetoCifrado[index]
      else:
          mensajeCifrado += caracter
  return mensajeCifrado

def descifrar (menCif):
  mensajeDescifrado= ""
  for caracter in menCif:
      if caracter in alfabeto:
          index = alfabetoCifrado.index(caracter)
          mensajeDescifrado +=  alfabeto[index]
      else:
          mensajeDescifrado +=  caracter
  return (mensajeDescifrado)

print (cifrar('I love you!'))
print (descifrar('R UY5Ñ 8Y4!'))