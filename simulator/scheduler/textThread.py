# -*- coding: utf-8 -*-
'''
Created on 21.02.2013

@author: steffi
'''

import random, time



'''def start():
	txtNr = random.randrange(0,2)
    txtAction = random.randrange(0,1)
	if txtAction == 0:
		# starte bearbeiten oder erstellen
		editDocuments()
	elif txtAction == 1:
		pass'''
		
def editDocuments(txtNr):
    txtPath = ""
    neueDatei = None
    print "txtnr" + str(txtNr)
    if txtNr == 0:
	txtPath = "/home/steffi/Dokumente/meineneuedatei.txt" 
	neueDatei = open(txtPath, "wb")
	neueDatei.write("test")  
    elif txtNr == 1:
	txtPath = "/home/steffi/Arbeitsfläche/TODOs.txt"
	neueDatei = open(txtPath, "wb")
	neueDatei.write("Einkaufen \n-Schuhe\n-Tasche\n\nGeburtstagsgeschenke\n-Mama\n-Oma")	
    elif txtNr == 2:
	txtPath = "/home/steffi/Dokumente/liste.txt" 
	neueDatei = open(txtPath, "wb")
   	neueDatei.write("Klagenfurt-Rom-Pompeij-Monaco-Barcelona-Bordeaux-Paris-Genf-Klagenfurt")
    else:
	txtPath = "/home/steffi/Dokumente/asdf.txt"	
	neueDatei = open(txtPath, "wb")
	neueDatei.write("test datei")
   		
    neueDatei.close()
    time.sleep(random.randrange(2,10))    

def deleteDocument():
   pass
