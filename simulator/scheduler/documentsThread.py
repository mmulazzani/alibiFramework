'''
Created on 15.02.2013

@author: steffi
'''

import threading
import os
import subprocess
import string
import random
import time

class DocumentsThread(threading.Thread):
    
    def __init__(self): 
        threading.Thread.__init__(self) 
        DocumentsThread.timer = False
        #variable um offene dokumente zu merken
    
    def run(self):  
        docsize = len(documents) - 1
        index = random.randint(0, docsize)
        
        if DocumentsThread.laststarted != None: 
            index = DocumentsThread.laststarted  
        
        
        DocumentsThread.laststarted = index
        os.system("/usr/bin/libreoffice -o " + str(documents[index]))
        time.sleep(5)
            
    def startLibreOfficeSimulation(self, count):
        self.__maximizeWindow()
        time.sleep(2)
        # neues dokument?
        time.sleep(random.randrange(1,5))            
        whatToDo = random.randrange(0,10) 
                
        if whatToDo == 3:
            print "insert text"
            self.__typeWord(text)
        elif whatToDo == 4:
            print "press return"
            subprocess.call(["xte", "key Return"])
        elif whatToDo == 6:
            print "press backspace"
            for i in range(0,1000):
                subprocess.call(["xte", "key BackSpace"])
                
        self.__saveDocument()
        self.shutdown()        
	'''if random.randint(0,1) == 0:
            self.shutdown()
            print "OO timer ist aus, OO wird beendet"
        else:
            print "OO timer ist aus, OO wird NICHT beendet "'''
            
        
    def __generateString(self, chars=string.ascii_uppercase + string.digits+ string.ascii_lowercase):
        size= random.randrange(1,15)
        return ''.join(random.choice(chars) for x in range(size))
   
    def __generateMouseClick(self):
        self.clickX = random.randrange(0,1366)
        self.clickY = random.randrange(0,768)
        command = "mousemove "+ str(self.clickX) + " "+ str(self.clickY)
        print command
        subprocess.call(["xte", command])
        subprocess.call(["xte", "mouseclick 1"])
        
    def shutdown(self):
        self.__saveDocument()
        print "beende libreoffice in 3 sek"
        time.sleep(3)
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key q"])
        subprocess.call(["xte", "keyup Control_L"])
        subprocess.call(["xte", "key Return"])
        # zuruecksetzen
        DocumentsThread.laststarted = None
        
        
    def __saveDocument(self):
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key s"])
        subprocess.call(["xte", "keyup Control_L"])
        time.sleep(3)
  
    def __typeWord(self, word):
        _key = ""
        for i in range(0, len(word)):
            time.sleep(0.3)
            _key = word[i]
            subprocess.call(["xte", "key "+_key])
        subprocess.call(["xte", "key space"])
    def __maximizeWindow(self):
        time.sleep(2)  
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key F10"])
        subprocess.call(["xte", "keyup Control_L"])
        print "Fenster maximiert"
     
def changeTimer(): 
    DocumentsThread.timer = True     

DocumentsThread.laststarted = None

text = ['Die vom uebrigen Tirol getrennte Geschichte Suedtirols beginnt im November 1918 mit der Besetzung durch italienische Truppen. \
Auf Grund des von OEsterreich-Ungarn am 3. November 1918 mit Italien geschlossenen Waffenstillstandsabkommens und dem Vertrag \
von Saint-Germain zwischen den Siegermaechten des Ersten Weltkrieges und der neu geschaffenen Republik Oesterreich fiel Suedtirol \
an das Koenigreich Italien und wurde zu dessen noerdlichster Provinz. Bei Texten ueber Suedtirol ist der historische Zusammenhang \
zu beachten: Bis 1918 und darueber hinaus war Suedtirol ein Begriff fuer alle historischen Landesteile Tirols suedlich des Brenners, \
bis ins 17. Jahrhundert noch ohne den Vintschgau und das Etschland, die zu Westtirol gerechnet wurden. Heute wird das Trentino, das \
 einstige Welschtirol, jedoch nicht mehr zu Suedtirol gezaehlt.', 
 'The history of the United Kingdom as a unified sovereign state began with the political union of the kingdoms of England, which the \
 husos Wales, and Scotland into a new kingdom called Great Britain. On this new state the historian Simon Schama said "What began as a\
  hostile merger would end in a full partnership in the most powerful going concern in the world... it was one of the most astonishing \
  transformations in European history."[1] A further Act of Union in 1800 added the Kingdom of Ireland to create the United Kingdom of \
  Great Britain and Ireland. The early years of the unified kingdom of Great Britain were marked by Jacobite risings which ended with  \
  defeat for the Stuart cause at Culloden in 1746. Later, in 1763, victory in the Seven Years War led to the dominance of the British \
  Empire, which was to be the foremost global power for over a century and grew to become the largest empire in history. As a result, \
  the culture of the United Kingdom, and its industrial, political, constitutional, educational and linguistic legacy, is widespread. \
In 1922, following the Anglo-Irish Treaty, Ireland effectively seceded from the United Kingdom to become the Irish Free State; a day later, \
Northern Ireland seceded from the Free State and became part of the United Kingdom. As a result, in 1927 the United Kingdom changed its formal \
title to the "United Kingdom of Great Britain and Northern Ireland,"[2] usually shortened to the "United Kingdom", the "UK" or "Britain". \
Former parts of the British Empire became independent dominions. In the Second World War, in which the Soviet Union and the US joined Britain \
as allied powers, Britain and its Empire fought a successful war against Germany, Italy and Japan. The cost was high and Britain no longer had \
the wealth or the inclination to maintain an empire, so it granted independence to most of the Empire. The new states typically joined the \
Commonwealth of Nations.[3] The United Kingdom has sought to be a leading member of the United Nations, the European Union and NATO, yet \
since the 1990s large-scale devolution movements in Northern Ireland, Scotland and Wales have brought into question the future viability \
of this constantly evolving political union.', '3 Punkte', 'TODO noch mal checken']
    
    
documents = ["/home/steffi/Dokumente/suedtirol.odt", "/home/steffi/Dokumente/british_history.odt", '/home/steffi/Dokumente/korrektur.ods', '/home/steffi/tests_und_dateien.ods']      
    
    
def openAndClosePdf():
    os.system('/usr/bin/gnome-open '+pdfs[random.randrange(0,len(pdfs)-1)])
    time.sleep(random.randrange(30,120))
    subprocess.call(["xte", "keydown Control_L"])
    subprocess.call(["xte", "key w"])
    subprocess.call(["xte", "keyup Control_L"])
    
pdfs = ["/home/steffi/Dokumente/fmi.pdf", "/home/steffi/Dokumente/Innovation.pdf"]
