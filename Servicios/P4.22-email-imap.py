import imaplib
  
user = 'jlcarnerosobrino@gmail.com'
password = 'poner aqui la contraseña'
imap_url = 'imap.gmail.com'
 
  
def search(key, value, con):  
  result, data = con.search(None, key, '"{}"'.format(value)) 
  return data 
  
def get_emails(result_bytes): 
  msgs = [] 
  for num in result_bytes[0].split(): 
    typ, data = con.fetch(num, '(RFC822)') 
    msgs.append(data) 
  return msgs 
  
con = imaplib.IMAP4_SSL(imap_url)    
con.login(user, password)    
con.select('Inbox')   
msgs = get_emails(search('FROM', 'jlcarnerosobrino@gmail.com', con)) 
    
for msg in msgs[::-1]:  
  for sent in msg: 
    if type(sent) is tuple:  
      content = str(sent[1], 'utf-8')  
      data = str(content) 
      try:  
        indexstart = data.find("ltr") 
        data2 = data[indexstart + 5: len(data)] 
        indexend = data2.find("</div>")   
        print(data2[0: indexend]) 

      except UnicodeEncodeError as e: 
        pass