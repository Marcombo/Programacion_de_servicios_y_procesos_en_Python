import socket
import threading
from tkinter import *

def conectarServidor():
  global client
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((SERVER, PORT))
  lblInfo["text"]= client.recv(1024).decode()
  
def inscribir ():
  global client
  client.sendall(bytes("#INSCRIBIR#"+entNombre.get() +"#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode()

def hiloJugada(cli, jug):
  cli.sendall(bytes("#JUGADA#"+jug+"#",'UTF-8'))
  lblInfo["text"]= cli.recv(1024).decode() 

def enviarJugada(jugada):  
  global client
  h = threading.Thread(target=hiloJugada, args=[client,jugada])
  h.start()
 
def consultaPuntos():
  global client
  client.sendall(bytes("#PUNTUACION#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode()  
  
#if __name__ == '__main__':
SERVER = "127.0.0.1"
PORT = 2000
client = None
informacion =""
fPPT = Tk() 
fPPT.title("Piedra-Papel-Tijera")
fPPT.geometry("300x300")
fPPT.resizable(True, True)
lblInfo = Label(fPPT, text=informacion)
lblInfo.place(x=0,y=230)
btnConn = Button(fPPT, text = 'Conectar', command = conectarServidor)
btnConn.place(x = 150,y = 50)
entNombre = Entry(fPPT)
entNombre.place(x = 20,y=100)
btnInscribir = Button(fPPT, text = 'Inscribir', command = inscribir)
btnInscribir.place(x = 150,y = 100)
btnPiedra = Button(fPPT, text = 'piedra', command = lambda: enviarJugada("piedra"))
btnPiedra.place(x = 50,y = 150)
btnPapel = Button(fPPT, text = 'papel', command = lambda: enviarJugada("papel"))
btnPapel.place(x = 100,y = 150)
btnTijera = Button(fPPT, text = 'tijera', command = lambda: enviarJugada("tijera"))
btnTijera.place(x = 150,y = 150)
btnPuntos = Button(fPPT, text = 'Puntuación', command =consultaPuntos)
btnPuntos.place(x = 150,y = 200)
fPPT.mainloop()