# -*- coding: utf-8 -*-
'''
Created on 13.02.2013

@author: steffi
'''

import threading
import os
import subprocess
import time
import string
import random



class ThunderbirdThread(threading.Thread):
    
    def __init__(self): 
        threading.Thread.__init__(self) 
        ThunderbirdThread.timer = False;

    def quitThunderbird(self):
        pass
    
    def run(self):
        os.system("/usr/bin/thunderbird")
        
    def readNewMessages(self):
        time.sleep(3)
        subprocess.call(["xte", "key n"])
        print "read new message"
        
    def writeEmail(self):
        time.sleep(3)
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key n"])
        subprocess.call(["xte", "keyup Control_L"])
        time.sleep(2)
        #an
        #subprocess.call(["xte", "key Tab"])
        emailIndex=random.randint(0,len(email)-1)
        self.__typeWord(email[emailIndex])
        time.sleep(2)
        #subprocess.call(["xte", "key Return"])
        
        
        #betreff
        mailIndex = random.randint(0,len(betreff)-1)
        subprocess.call(["xte", "key Tab"])
        self.__typeWord(betreff[mailIndex])
        
        subprocess.call(["xte", "key Tab"])
        
        print "write email"
        self.__writeContextAndSendEmail(mailIndex)
        
        
    def __writeContextAndSendEmail(self, index):
        self.__typeWord(inhalt[index])
        
        subprocess.call(["xte", "key Return"])
                
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key Return"])
        subprocess.call(["xte", "keyup Control_L"])
        
        time.sleep(1)
        
        subprocess.call(["xte", "key Return"])
        
    def __typeWord(self, word):
        spell = ""
        for i in range(0, len(word)):
            time.sleep(0.1)
            #special character
            if spell == "/":
                spell = "/"+word[i]
            else:    
                spell = word[i]
                
            # todo algorithmus der entescheidet wegen zeichen            
            if spell == "@":
                subprocess.call(["xte", "keydown Control_L"])
                subprocess.call(["xte", "key at"])
                subprocess.call(["xte", "keyup Control_L"])
            #sonderzeichen
            elif spell not in string.ascii_letters:
                spell = keySyms[spell]
                #sonderzeichen mit shift
                if spell in upKeys:
                    subprocess.call(["xte", "keydown Shift_L"])
                    subprocess.call(["xte", "key "+spell])
                    subprocess.call(["xte", "keyup Shift_L"])
                #sonderzeichen mit altgr   
                elif spell in altGrKeys:
                    subprocess.call(["xte", "keydown Alt_R"])
                    subprocess.call(["xte", "key "+spell])
                    subprocess.call(["xte", "keyup Alt_R"])
                else:     
                    subprocess.call(["xte", "key "+spell])
            elif spell == "ß":
                spell = "question"
                subprocess.call(["xte", "key "+spell])
            else:    
                subprocess.call(["xte", "key "+spell])
            
                
    def closeThunderbird(self):
        print "beende thunderbird in 5 sek"
        time.sleep(5)
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key q"])
        subprocess.call(["xte", "keyup Control_L"])
        ThunderbirdThread.timer = True
        
    def respondEmail(self):
        time.sleep(3)
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key r"])
        subprocess.call(["xte", "keyup Control_L"])
        time.sleep(2) 
        print "respond email"
        self.__writeContextAndSendEmail(random.randint(0,len(betreff)-1))
        
    def fowardEmail(self):
        time.sleep(3)
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key l"])
        subprocess.call(["xte", "keyup Control_L"])
        time.sleep(2)
        self.__typeWord("beyer.stefanie")
        time.sleep(2)
        subprocess.call(["xte", "key Tab"])
        subprocess.call(["xte", "key Tab"])
        print "foward email"
        self.__writeContextAndSendEmail(random.randint(0,len(betreff)-1))
        
    def deleteEmail(self):
        time.sleep(2)
        subprocess.call(["xte", "key Delete"])
        print "email wurde geloescht"
        
    def shutdown(self):
        self.closeThunderbird()
                
                
def changeTimer(): 
    ThunderbirdThread.timer = True
            
betreff = ['email', 'besuch', 'kino', 'geburtstag', 'kino', 'DANKE :-)', 'Urlaub', 'OK']

inhalt = ['hi \ndanke, hab deine nachricht bekommen. bin grad im stess und meld mich dann, wenn ich zeit hab\nlg',
'passt, geht in ordnung!\nlg','hallo, \nwann wolltest du ins kino gehen?\nlg', 'danke, fuer deine einladung, komme gerne!', 
'hey, \nwelchen film würdest du gern im kino sehen?\nlg ', 'hey du, \nvielen Dank, dass du dir das angeschaut hast!\nbis bald!\nlg', 
'Hey, \nhast du heuer schon urlaub gebucht? ich fahr nach Italien und wollte fragen, ob du Lust hast mitzukommen. \nIch plane ein kleines Haus zu mieten - direkt am Meer.\nNa, was sagst du? Meld dich! \nlg ',
'Geht in ordnung!\n LG']
            
email = ['beyer.margit', 'christian.macho', 'beyer.margit', 'beyer.stefanie', 'beyer.margit', 'stefanie.beyer', 'steffisp', 'beyer.margit']    
            
upKeys = ['question', 'exclam', 'numbersign', "percent", 
          "dollar", "ampersand", "quotedbl", "apostrophe", 
          "parenleft", "parenright", "asterisk", "equal", 
          "slash", "colon", "semicolon", "greater"
]

altGrKeys = [ "at", "bracketleft", "bracketright", "backslash",
            "asciicircum", "underscore", "grave", "braceleft", "bar",
            "braceright", "asciitilde"]
        
        
keySyms = {
    ' ' : "space",
    '\t' : "Tab",
    '\n' : "Return",  # for some reason this needs to be cr, not lf
    '\r' : "Return",
    '\e' : "Escape",
    '!' : "exclam",
    '#' : "numbersign",
    '%' : "percent",
    '$' : "dollar",
    '&' : "ampersand",
    '"' : "quotedbl",
    '\'' : "apostrophe",
    '(' : "parenleft",
    ')' : "parenright",
    '*' : "asterisk",
    '=' : "equal",
    '+' : "plus",
    ',' : "comma",
    '-' : "minus",
    '.' : "period",
    '/' : "slash",
    ':' : "colon",
    ';' : "semicolon",
    '<' : "less",
    '>' : "greater",
    '?' : "question",
    '@' : "at",
    '[' : "bracketleft",
    ']' : "bracketright",
    '\\' : "backslash",
    '^' : "asciicircum",
    '_' : "underscore",
    '`' : "grave",
    '{' : "braceleft",
    '|' : "bar",
    '}' : "braceright",
    '~' : "asciitilde"
    }
                  
