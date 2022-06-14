from os import system
import subprocess
import asyncio

def showNotepad1():  
  try:
    subprocess.run(['Notepad.exe',])
  except subprocess.CalledProcessError as e:
      print(e.output)
async def showNotepad2():  
  try:
    await asyncio.create_subprocess_exec('notepad.exe')
  except subprocess.CalledProcessError as e:
      print(e.output)

async def main():
  print ("inicio llamada síncrona")
  showNotepad1()
  print ("fin llamada síncrona")
  print ("inicio llamada asíncrona")
  await showNotepad2()
  print ("fin llamada asíncrona")
  print("pulsa una tecla para terminar")
  system ('Pause')
  
asyncio.run(main())