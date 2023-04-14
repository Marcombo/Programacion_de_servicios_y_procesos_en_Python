import socket
from tkinter import *
import tkinter

def conectarServidor():
  global client
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((SERVER, PORT))
  lblInfo["text"]= client.recv(1024).decode()
  btnConn["state"]=DISABLED
  btnInscribir["state"]=NORMAL
  
def inscribir ():
  global client
  client.sendall(bytes("#INSCRIBIR#"+entNombre.get() +"#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode()
  btnInscribir["state"]=DISABLED
  btnPiedra["state"]=NORMAL
  btnPapel['state']=NORMAL
  btnTijera["state"]=NORMAL

def enviarJugada(jugada):  
  global client
  btnPiedra["state"]=DISABLED
  btnPapel['state']=DISABLED
  btnTijera["state"]=DISABLED
  client.sendall(bytes("#JUGADA#"+jugada+"#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode() 
  btnPiedra["state"]=NORMAL
  btnPapel['state']=NORMAL
  btnTijera["state"]=NORMAL
  btnPuntos["state"]=NORMAL
    
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
btnInscribir = Button(fPPT, text = 'Inscribir', command = inscribir, state=DISABLED)
btnInscribir.place(x = 150,y = 100)
btnPiedra = Button(fPPT, text = 'piedra', command = lambda: enviarJugada("piedra"), state=DISABLED)
btnPiedra.place(x = 50,y = 150)
btnPapel = Button(fPPT, text = 'papel', command = lambda: enviarJugada("papel"), state=DISABLED)
btnPapel.place(x = 100,y = 150)
btnTijera = Button(fPPT, text = 'tijera', command = lambda: enviarJugada("tijera"), state=DISABLED )
btnTijera.place(x = 150,y = 150)
btnPuntos = Button(fPPT, text = 'Puntuación', command =consultaPuntos, state=DISABLED )
btnPuntos.place(x = 150,y = 200)
fPPT.mainloop()