import webbrowser 

url1 = 'https://www.marcombo.com/'
url2 = 'https://www.amazon.es/'
url3 = 'https://www.google.com/'

# Abrir la URL en una nueva pestaña si ya existe una ventana del navegador abierta
webbrowser.open_new_tab(url1)

# Abrir la URL en una nueva ventana, si es posible
webbrowser.open_new(url2)

edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
webbrowser.get('edge').open_new(url3)
