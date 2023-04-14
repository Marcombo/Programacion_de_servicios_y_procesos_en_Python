from urllib import request

response = request.urlopen('http://www.python.org')

print('RESPONSE:', response)
print('CODIGO HTTP: ', response.getcode())
print('URL     :', response.geturl())

headers = response.info()
print('DATE    :', headers['date'])
print('HEADERS :')
print('---------')
print(headers)

print('BODY   :')
print('---------')
for _ in range (20):
  linea = response.readline().decode('utf-8')
  print(linea)