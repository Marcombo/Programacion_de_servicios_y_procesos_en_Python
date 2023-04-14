import ftplib
#creadenciales FTP, la contraseña la cambian cada cierto tiempo
FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"

def listCallback(line):
    print(line)

# conexión al servidor de FTP
ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
#forzar codificación UNICODE
ftp.encoding = "utf-8"
welcomeMessage = ftp.getwelcome()
print(welcomeMessage)

#se puede obtener la respuesta a través de una función de callback
respMessage = ftp.retrlines("LIST", listCallback)
#también se puede obtener el resultado de forma directa
#respMessage = ftp.retrlines("LIST")
print ("-----------------------------")
print(respMessage)

#cerrar la conexión
ftp.quit()