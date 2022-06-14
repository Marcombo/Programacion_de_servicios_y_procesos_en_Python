import threading

def f():
  pass   

try:
  t = threading.Thread(target=f)
  t.start()
  t.start()
except Exception as e:
  print("Error:", e)
print ("Final del programa")
 