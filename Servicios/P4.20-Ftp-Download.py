import ftplib
#creadenciales FTP, la contraseña la cambian cada cierto tiempo
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

try:
  # conexión al servidor de FTP
  ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
  #forzar codificación UNICODE
  ftp.encoding = "utf-8"
  welcomeMessage = ftp.getwelcome()
  print(welcomeMessage)

  #bajamos el fichero subido anteriormente y lo renombramos a bajado.txt
  fichero_enServidor = "subido.txt"
  fichero_local = "bajado.txt"
  with open(fichero_local, "wb") as file:
      # usamos el comando RETR para descargar
      ftp.retrbinary(f"RETR {fichero_enServidor}", file.write)
      
  #cerrar la conexión
  ftp.quit()
except ftplib.all_errors as e:
  errorcode_string = str(e).split(None, 1)[0]