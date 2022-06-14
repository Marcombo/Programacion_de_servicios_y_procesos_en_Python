import subprocess

# obtención de los procesos
Datos = subprocess.check_output(['wmic', 'process', 'list', 'brief'])
a = str(Datos)
try:
	for i in range(len(a)):
		print(a.split("\\r\\r\\n")[i])
except IndexError as e:
	print("Finalizado")
