# einige kleine Helfer.


# License
Autor: Ralf Weinert 
Email: ralf.weinert@gmx.de
cc-by-sa 4.0 
https://creativecommons.org/licenses/by-sa/4.0/deed.de

# Das Script *Laptops_PDF_erzeugen.py* erzeugt eine PDF mit 4*2 QR
Zum Ausdrucken eignen sich 'Adress labels' mit der Größe
99,1 mm x 67,7 mm in der Anordnung 
Din A 4 mit 4 Reihen und 2 Spalten   

Die QR werden in Verzeichnis *path* abgelegt.
Das script durchsucht das Verzeichnis  
- nach Bildern des Typ *pic_format*
- und einem String im Namen *filename_contains* 

Das fertige PDF wird in *path* abgelegt

Probleme
*path* muss mit einem schließenden '/' versehen sein

# Das Script *Laptops_QR_erzeugen.py* erzeugt QR
In *data* wird der Inhalt zum QR hinterlegt.
In diesem Fall eine Email,
Darum muss *email*, *subject* und *body* befüllt werden.

Die QR werden in Verzeichnis *path* abgelegt.
Es werden Bilder im Format: *pic_format* angelegt.
*data* wird mit iso-8859-1 codiert, damit das mit den Umlauten klappt.

Probleme
*path* muss mit einem schließenden '/' versehen sein


