from cmath import inf
from re import I
import socket
import threading
from tkinter import *

def conectarServidor(puertoCallback):
  global client
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((SERVER, PORT))
  lblInfo["text"]= client.recv(1024).decode()
  t = threading.Thread(target=escucharRespuestas, args=(puertoCallback))
  t.daemon=True
  t.start()
  
  
def inscribir (puerto):
  global client
  client.sendall(bytes("#INSCRIBIR#"+entNombre.get() +"#"+puerto+"#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode()

def enviarJugada(jugada):  
  global client
  client.sendall(bytes("#JUGADA#"+jugada+"#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode() 
  
def consultaPuntos():
  global client
  client.sendall(bytes("#PUNTUACION#",'UTF-8'))
  lblInfo["text"]= client.recv(1024).decode()    
  
def escucharRespuestas(puertoCallBack):
  with  socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((SERVER, puertoCallBack))
    print("Escucha en callback")
    s.listen()
    while True:
      (cli,add) = s.accept()
      with cli:
        data = cli.recv(512).decode("utf_8")
        print ("Enviado desde cliente:<",data,">")      
        cli.send(bytes("#OK#",'UTF-8'))

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
lblPuerto = Label(fPPT, text="Puerto de escucha:")
lblPuerto.place(x=0,y=50)
entPuerto = Entry(fPPT,)
entPuerto.place(x = 110,y=50, width=30)
btnConn = Button(fPPT, text = 'Conectar', command = lambda: conectarServidor(int(entPuerto.get())))
btnConn.place(x = 150,y = 50)
entNombre = Entry(fPPT)
entNombre.place(x = 20,y=100)
btnInscribir = Button(fPPT, text = 'Inscribir', command = lambda: inscribir(entPuerto.get()))
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