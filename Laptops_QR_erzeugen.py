#!/usr/bin/env python
#!/usr/bin/env python

# Autor: Ralf Weinert 
# Email: ralf.weinert@gmx.de 
#
# Das Script *Laptops_QR_erzeugen.py* erzeugt QR
# In *data* wird der Inhalt zum QR hinterlegt.
# In diesem Fall eine Email,
# Darum muss *email*, *subject* und *body* befüllt werden.
#
# Die QR werden in Verzeichnis *path* abgelegt.
# Es werden Bilder im Format: *pic_format* angelegt.
# *data* wird mit iso-8859-1 codiert, damit das mit den Umlauten klappt.
#
# Probleme
# *path* muss mit einem schließenden '/' versehen sein

#License
# cc-by-sa 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/deed.de


import pyqrcode
from pyqrcode import QRCode

# Speicherpfad der QR
# dieser muss existieren!
# ifExist wird nicht geprüft!!!!
# MIT schließenem '/'
path = r"/home/ralf/programmieren/phython_scipts/Laptop_QR/"

# pic_format
pic_format = ".png"

# Name für den QR-Code, dieser wird mit einer Zahl *n* = range(min,max) ergänzt
qr_name = "Laptop"

# QR - Types:
qr_types = "email"

# allgemeine Angaben
email = "computer@seewiesenschule.de"
subject = "Laptop "
body = """Lieber Admin, 

	Leider macht der Laptop Probleme. 
	Beschreibung des Problem: 
	O keine Anmeldung möglich 
	O Domäne wird nicht gefunden 
	O Abmelden dauert sehr lange 
	O ...
	
	Liebe Grüße
	"""
# Anzahl der QR-Codes
n = range(1,31)



# erzeuge die QR-Codes
for i in n:
	if qr_types == "email":
		data = 'mailto:'+email+'?subject='+subject+str(i)+'&body='+body
	else:
		print("Es wird nur der Typ Email untersützt")
	print (data)	
	myQR = QRCode(data.encode('iso-8859-1'), encoding='iso-8859-1')
	if pic_format == ".png":
		myQR.png(path+qr_name+str(i)+'.png', scale=16)
	else:
		print("Dieses Format *"+pic_format+"* wird nicht unterstützt")
		
