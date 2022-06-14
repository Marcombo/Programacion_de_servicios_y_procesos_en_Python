#instalar previamente: "pip install pywin32"
import win32clipboard

#enviar datos al portapapeles
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText("MARCOMBO")
win32clipboard.CloseClipboard()

# obtener datos del portapapeles
win32clipboard.OpenClipboard()
datos = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
print (datos)
