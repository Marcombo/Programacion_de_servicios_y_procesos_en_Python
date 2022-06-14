import threading 
    
algo = 0
  
lock = threading.Lock() 
  
lock.acquire() 
algo +=1
  
lock.acquire()  
algo += 2
lock.release() 
  
print(algo) 