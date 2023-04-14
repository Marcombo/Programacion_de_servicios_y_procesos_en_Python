import ftplib
#creadenciales FTP, la contraseña la cambian cada cierto tiempo
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

def listCallback(line):
  print(line)

try:
  # conexión al servidor de FTP
  ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
  #forzar codificación UNICODE
  ftp.encoding = "utf-8"
  welcomeMessage = ftp.getwelcome()
  print(welcomeMessage)

  #fichero a subir
  filename = "subido.txt"
  with open(filename, "rb") as file:
    # Usamos comando STOR para subirlo
    ftp.storbinary(f"STOR {filename}", file)
  # listamos el contenido para comprobar
  ftp.dir(listCallback)

  #cerrar la conexión
  ftp.quit()
except ftplib.all_errors as e:
  errorcode_string = str(e).split(None, 1)[0]