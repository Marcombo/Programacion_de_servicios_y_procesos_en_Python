from urllib import parse
from urllib import request
import json

#diccionario de datos a enviar
datos_consulta = {'cod-persona':245}
#codificación de los datos
encoded_args = parse.urlencode(datos_consulta).encode('utf-8')
#endpoint de nuestra petición
url = 'https://psp-api.free.beeceptor.com/persona'
#composición de la petición con la url y los datos POST a insertar en el header
response = request.urlopen(url, encoded_args).read().decode('utf-8')
#print(response)
datos = json.loads(response)
print ("Nombre: ", datos["nombre"])
print ("Edad: ", datos["edad"])
