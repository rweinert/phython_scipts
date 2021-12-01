#!/usr/bin/env python

# Autor: Ralf Weinert 
# Email: ralf.weinert@gmx.de 
#
# Das Script *Laptops_PDF_erzeugen.py* erzeugt eine PDF mit 4*2 QR
# Zum Ausdrucken eignen sich 'Adress labels' mit der Größe
# 99,1 mm x 67,7 mm in der Anordnung 
# Din A 4 mit 4 Reihen und 2 Spalten   
# 
# Die QR werden in Verzeichnis *path* abgelegt.
# Das script durchsucht das Verzeichnis  
# - nach Bildern des Typ *pic_format*
# - und einem String im Namen *filename_contains* 
#
# Das fertige PDF wird in *path* abgelegt
#
# Probleme
# *path* muss mit einem schließenden '/' versehen sein

#License
# cc-by-sa 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/deed.de

from fpdf import FPDF

# für den Import der QR/Bilder
import os

# Allgemeines

# Wo sind die QR abgelegt? - Pfad zum Verzeichnis
# MIT schließenem '/'
path = r"/home/ralf/programmieren/phython_scipts/Laptop_QR/"

# pic_format
pic_format = ".png"

# filename_contains
filename_contains = "Lap" 

# Daten für den Din A4 ausdruck
# eine Zelle für Avery L3165
cell_width = 99.1
cell_hight = 65.45 # sollte 67.7 sein, angepasst durch 'Pobieren'
page_border = 15.1
cell_in_col = 4

# Name der zuerstellenden PDF-Datei
pdf_name = "QR_Laptop1_30.pdf"

### Beginn Script

# path is a directory of which you want to list
filelist = os.listdir( path )
 
# Array für die Bilder - hier werden die Bilder als Filename gespeichert
my_file_list = []
 
 
# Diese Forschleife durchläuft alle Einträge in *filelist*
# und sucht die passenden mit 
# - pic_format 
# und 
# - filename_contains

#print("orginale Filelist")
#print(filelist)
for fichier in filelist:
    if not(fichier.endswith(pic_format)):
        filelist.remove(fichier)
#print("nach Filter *.png")
#print(filelist)
        
for file_name in filelist:
	if file_name.__contains__(filename_contains):
		print(file_name)
		my_file_list.append(path+file_name)
#print("als Dateinmen für das PDF")
#print(my_file_list)



# Initialisiere das PDF und lege das Format fest
#pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf = FPDF(orientation='P', unit='mm', format=(210, 297))

# Ränder setzen
pdf.set_top_margin(15.1)
pdf.set_left_margin(5.9)


# erzeuge eine Seite
pdf.add_page()
pdf.set_font('Arial', 'B', 16)



# pdf.cell Werte
#cell_in_row = 2
#border = 1
#new_line = 0

# zum Testen
#pdf.line(10,0,10,15.1)
#pdf.line(55,281.9,55,297)


# Grenzlinen zum Testen
pdf.line(105,0,105,297)
for i in range(cell_in_col+1):
	pdf.line(page_border,page_border+i*cell_hight,194.9,page_border+i*cell_hight)

col = 0 # links 0 und rechts 1
row = 0 # zählt durch bis 8

## offset und Größe für den QRCode
qr_offset_x = page_border + 10
qr_offset_y = page_border + 2.5
qr_size = 60

# Zähler über die QR-Codes
my_index = 0

# diese Schleife erzeugt die 2 Spalten ind 4 Reihen
# immer nach 8 Einträgen kommt einen neue Seite
for qrcode_name in my_file_list:
	img_x = qr_offset_x + col * cell_width
	img_y = qr_offset_y + row * cell_hight
	pdf.image(qrcode_name, img_x, img_y , qr_size,qr_size)
	my_index+=1
	if col == 0:
		col = 1
	else:
		col = 0
		row+= 1
	if row == 4:
		row = 0
		pdf.add_page()
		pdf.line(105,0,105,297)
		for i in range(cell_in_col+1):
			pdf.line(page_border,page_border+i*cell_hight,194.9,page_border+i*cell_hight)
		
    

# Erzeuge das PDF-File
pdf.output(path+pdf_name, 'F')

