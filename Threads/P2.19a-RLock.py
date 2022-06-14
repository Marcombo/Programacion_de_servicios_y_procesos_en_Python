import threading 
  
algo = 0
  
rlock = threading.RLock() 
  
rlock.acquire() 
algo += 1
  
rlock.acquire()  
algo += 2
rlock.release() 
rlock.release() 
  
print(algo) 