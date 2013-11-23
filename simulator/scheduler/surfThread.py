# -*- coding: utf-8 -*-

import subprocess
import random
from splinter import Browser
from splinter import exceptions
import time
import threading
from selenium.common.exceptions import ElementNotVisibleException
from splinter.exceptions import ElementDoesNotExist
from urllib2 import URLError
import string
import constants
import shutil, os

class SurfThread(threading.Thread):

   
    def __init__(self, hoehe, breite, _format):
        threading.Thread.__init__(self) 
        self.seiten = []
        self.words = []
        self.toWait = None
        self.elemNo = None
        self.wordNo = None
        self.clickNo = None
        self.clickX = None
        self.clickY = None
        self.back = None
        self.changeTabs = None
        self.__browser = Browser("firefox", profile=constants.profile)
        time.sleep(5)
        #self.__maximizeWindow()
        #time.sleep(5)        
        SurfThread.timer = False
        SurfThread.hoehe = hoehe
        SurfThread.breite = breite 
        SurfThread._format = _format


    def __readData(self):
        # read homepages to visit 
        surfListe = open("/home/steffi/Dokumente/surfListe.txt", "rb")
        for line in surfListe: 
            self.seiten.append(line)
        surfListe.close()
        # read words for search in google, wikipedia, amazon, youtube
        keyWords = open("/home/steffi/Dokumente/keyWords.txt", "rb").readlines()
        for line in keyWords: 
            self.words.append(line.decode("utf-8"))
        #keyWords.close(), 
    print "data read"
    
    
    def run(self):
        
        self.__readData()    
       
        rand = random.randint(2,5)
        for i in range(0, rand):
            print "noch "+ str(i) +" mal"
	    print "TIMER:" +str(SurfThread.timer)
            if SurfThread.timer == False :
            
                self.__generateRandom()
                    
                print "visit: "+self.seiten[self.elemNo]
                self.__visitHomepage( self.seiten[self.elemNo].strip())
                print "clickNo: "+ str(self.clickNo)
		print "towait = "+ str(self.toWait)
                time.sleep(self.toWait)
                for i in range(self.clickNo):
                    time.sleep(random.randrange(5,10))
                    if i % 2 == 0:
                        self.__generateRandomClick()
                    if i == 2:
                        self.__pageDown()
                        time.sleep(random.randrange(1,5))
                    if i == (self.clickNo-1):
                        self.__pageBottom()
                        time.sleep(random.randrange(2,10))
                    if i%2 == 0 and self.back == 1:
                        self.__goBack()
                        time.sleep(random.randrange(2,10))  

    	path = self.__browser.driver.firefox_profile.profile_dir
    	print path
    	os.remove(constants.profile+'/places.sqlite')
    	shutil.copyfile(path+'/places.sqlite', constants.profile+'/places.sqlite')
        self.__closeWindow()
    	shutil.rmtree(path)
    	#os.rmdir(path)
        print "Firefox beendet"
        
        
    def starte(self):
        self.run()
    
    def __generateRandom(self):
        self.toWait = random.randrange(5,45)
        self.elemNo = random.randrange(0,len(self.seiten))
        self.clickNo = random.randrange(2,7)
        self.back = random.randrange(0,10)
        self.wordNo = random.randrange(0, len(self.words))
    
    def __generateRandomClick(self):
        self.clickX = random.randrange(100,constants.BREITE - 50) #1366
        self.clickY = random.randrange(50,constants.HOEHE-50) #768
        command = "mousemove "+ str(self.clickX) + " "+ str(self.clickY)
        print command
        subprocess.call(["xte", command])
        subprocess.call(["xte", "mouseclick 1"])
      
    def __followLink(self, text, index=0):
        if index == None:
            index = 0
        
        try:   
            self.__browser.click_link_by_partial_text(text)[index]
        except ElementDoesNotExist:
            print "Element does not exist"
        except TypeError:
            print "Type Error"
        except Exception as e: 
	       print "nix passiert" + e
    
    def __visitGooglePage(self, url):
             
        print "google"
        
        self.__browser.visit(url)
        time.sleep(random.randrange(2,15))
        searchWord = str(self.words[self.wordNo]).strip().decode("utf-8")
        print searchWord
        self.__fillInput('q', searchWord)
        time.sleep(random.randrange(2,15))
        self.__findElementAndClick("btnG", "name", None)
        subprocess.call(["xte", "key Return"])
        wordSplit = str(searchWord).split(" ")
        time.sleep(random.randrange(10,30))
            #baaaad practice
        try:
            self.__followLink(wordSplit[0], self.wordNo%10)
        except Exception:
            try: 
                self.__followLink(wordSplit[1], self.wordNo%10)
            except Exception:
                    pass
        
        
    def __visitHomepage(self, url):
       
        clickNoMod4 = self.clickNo % 4
        toWaitMod4 = self.toWait % 4
        
        if "google" in url:
            self.__visitGooglePage(url)
        elif "wikipedia" in url:
            self.__visitWikipediaPage(url)
        elif "amazon" in url:
            self.__visitAmazonPage(url)
        elif "ebay" in url:
            self.__visitEbayPage(url)
        elif "youtube" in url:
            print "youtube"
            self.__watchYoutubeVideo(url)
        elif "facebook" in url:
            print "facebook"
            self.__visitFacebook(url)
        elif "twitter" in url:
            print "twitter"
            self.__twitterSomething(url)
        else:
	    try:
            	self.__browser.visit(url)
	    except Exception as e:
		print e
		pass
        
       
    def __goBack(self): 
        self.__browser.back()
        
    def shutdown(self):
        print "setze timer um und beende firefox"
        changeTimer()
        
    def __fillInput(self, _id, _input):
        try:
            self.__browser.fill(_id, _input)
        except Exception as e:
            print e.message
            pass
        
    def __findElementAndClick(self, name, identifier, index):
        #check falls keine nummer mitgenommen wurde
        if index == None:
            index = 0
        #suche nach elementen
        try:
            if identifier == "name":
                button = self.__browser.find_by_name(name)[index]
            elif identifier == "id":
                button = self.__browser.find_by_id(name).click
            
                button.click()
        except (exceptions.ElementDoesNotExist, ElementNotVisibleException, URLError):
            print "ElementDoesnotExist OR ElementNotVisible OR URLError"
            pass
	except Exception as e:
	    print e
	    pass
        
    def __closeWindow(self):
        time.sleep(3)  
        subprocess.call(["xte", "keydown Control_L"])
        #subprocess.call(["xte", "keydown Shift_L"])
        subprocess.call(["xte", "key q"])
        #subprocess.call(["xte", "keyup Shift_L"])
        subprocess.call(["xte", "keyup Control_L"])
        print "Fenster geschlossen"
    
    def __maximizeWindow(self):
        time.sleep(2)  
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key F10"])
        subprocess.call(["xte", "keyup Control_L"])
        print "Fenster maximiert"
    
    def __pageDown(self):
        time.sleep(3)
        subprocess.call(["xte", "key Page_Down"])
    
    def __pageBottom(self):
        subprocess.call(["xte", "key End"])
    
    def __watchYoutubeVideo(self, url):
        self.__browser.visit(url)
        time.sleep(random.randrange(2,15))
        
        searchWord = str(self.words[self.wordNo]).strip().decode("utf-8")
        print searchWord
        
        self.__fillInput('search_query', searchWord)
        time.sleep(random.randrange(2,15))

        subprocess.call(["xte", "key Return"])
        time.sleep(random.randrange(2,15))
        
	#nur bei 16:9 monitor
        index = None
        breite = 0
	if SurfThread._format == "16:9":

            index = [int(SurfThread.hoehe // 4.59), 
                     int(SurfThread.hoehe // 3.04),
                     int(SurfThread.hoehe // 2.22),
                     int(SurfThread.hoehe // 1.77)]
            breite = int(SurfThread.breite//4.74)
        else:
            index = [int(SurfThread.hoehe // 4.10), 
                     int(SurfThread.hoehe // 2.19),
                     int(SurfThread.hoehe // 1.54),
                     int(SurfThread.hoehe // 1.28)]
	    breite = int(SurfThread.breite//2.15)
                
        #self.__followLink(searchWord, None)
        #235 1 - 355 2 - 4853   
        rand = random.randint(0, (len(index)-1))
        subprocess.call(["xte", "mousemove "+ str(breite) + " " +str(index[rand])])
        time.sleep(random.randrange(2,15))
        subprocess.call(["xte", "mouseclick 1"])
        
        time.sleep(5)
        print "mousemove + anschauen"
    
        #breite höhe von links oben
        #subprocess.call(["xte", "mousemove "+ str(int(SurfThread.breite//3.17)) + " " + str(int(SurfThread.hoehe//3.2225))])
        #time.sleep(2)
        subprocess.call(["xte", "mouseclick 1"])
        #todo mehr zeit
        time.sleep(random.randrange(2,45))
        
    
        
        
    def __visitWikipediaPage(self, url):
        print "wikipedia"
        
        self.__browser.visit(url)
        time.sleep(2)
        searchWord = str(self.words[self.wordNo]).strip().decode("utf-8")
        print searchWord
        self.__fillInput('search', searchWord)
        time.sleep(random.randrange(2,15))
        subprocess.call(["xte", "key Return"])
        wordSplit = str(searchWord).split(" ")
        time.sleep(2)    
            #baaaad practice
        try:
            self.__followLink(wordSplit[0], self.wordNo%10)
        except Exception:
            try: 
                self.__followLink(wordSplit[1], self.wordNo%10)
            except Exception:
                    pass
                
    def __visitAmazonPage(self, url):
        print "amazon"
        
        self.__browser.visit(url)

        time.sleep(random.randrange(2,15))
        searchWord = str(self.words[self.wordNo]).strip().decode("utf-8")
        print searchWord
        self.__fillInput('field-keywords', searchWord+'\n')
        time.sleep(2)
       
	subprocess.call(["xte", "key Return"])
        
        wordSplit = str(searchWord).split(" ")
        time.sleep(random.randrange(2,15))  
            #baaaad practice
        try:
            self.__followLink(wordSplit[0], self.wordNo%10)
        except Exception:
            try: 
                self.__followLink(wordSplit[1], self.wordNo%10)
            except Exception:
                    pass
    
    def __visitEbayPage(self, url):
        print "ebay"
        
        self.__browser.visit(url)
        time.sleep(random.randrange(2,15))
        searchWord = str(self.words[self.wordNo]).strip().decode("utf-8")
        print searchWord
        self.__typeWord(searchWord)
        time.sleep(random.randrange(2,15))
        subprocess.call(["xte", "key Return"])
        wordSplit = str(searchWord).split(" ")
        time.sleep(random.randrange(2,15))
            #baaaad practice
        self.__followLink(wordSplit[0], self.wordNo%10)
        
    def __visitFacebook(self, url):
        print "facebook"
        
        self.__browser.visit(url)
        time.sleep(random.randrange(2,15))
        
        #gegenebenefalls einloggen
        if self.__browser.is_text_present(constants.FB_USER) == False:
            print "noch nicht eingeloggt"
            self.__fillInput('email', constants.FB_EMAIL)
            time.sleep(2)
            self.__fillInput('pass', constants.FB_PW)
            time.sleep(2)
            subprocess.call(["xte", "key Return"])
            time.sleep(5)
            
    def __twitterSomething(self, url):
        print "twitter"
        
        self.__browser.visit(url)
        time.sleep(random.randrange(2,15))
        #todo wenns tart seite nicht sichtbar, einloggen
        if self.__browser.is_text_present('Startseite') == False:
            print "noch nicht eingeloggt"
            
            '''name = self.__browser.find_by_name('session[username_or_email]').first
            if name != None:
                print "name gefunden"
            name.click()
            time.sleep(3)
            self.__typeWord('steffi_spam')
            
            passW = self.__browser.find_by_id('signin-password').first
            passW.click()
            time.sleep(3)
            self.__typeWord('steffispam')'''
            
            
            #self.__fillInput("session[username_or_email]", "steffispam@anoome.at")
            #time.sleep(2)
            #self.__fillInput('signin-pass', "steffispam")
            #self.__fillInput('signin-pass', "session[password]")
            #time.sleep(2)
            #subprocess.call(["xte", "key Return"])
            #time.sleep(5)
            
            # so gehts 13.5.13
            time.sleep(random.randrange(2,15))
            subprocess.call(["xte", "key Tab"])
            time.sleep(3)
            subprocess.call(["xte", "key Tab"])
            time.sleep(3)
            subprocess.call(["xte", "key Tab"])
            time.sleep(random.randrange(2,15))
            self.__typeWord(constants.TWITTER_USER)
            subprocess.call(["xte", "key Tab"])
            time.sleep(2)
            self.__typeWord(constants.TWITTER_PW)
            time.sleep(2)
            subprocess.call(["xte", "key Return"])
            time.sleep(random.randrange(2,15))
            ''' self.__followLink("Kleine Zeitung")
           # time.sleep(5)
           # self.back()
           # self.__followLink("ORF Sport")
           # time.sleep(5)
           # self.back()'''
        
        self.__followLink("Startseite")
        time.sleep(3)
        print "input twitter"
        field = self.__browser.find_by_id("tweet-box-mini-home-profile").first
        field.click()
        print "geklickt"
        self.__typeWord(twittertext[random.randrange(0,len(twittertext)-1)])
        time.sleep(random.randrange(2,15))
        subprocess.call(["xte", "key Tab"])
        time.sleep(2)   
        subprocess.call(["xte", "key Return"])
        print "tweet gepostet"
        
            
            
    def __typeWord(self, word):
        spell = ""
        for i in range(0, len(word)):
            #special character
            if spell == "/":
                spell = "/"+word[i]
            else:    
                spell = word[i]
                
            # todo algorithmus der entescheidet, zuerst spezialzeichen oder normales zeichen               
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

twittertext = ['#weather sunshine :)', '#oebb zugfahren macht freude...'] 
             
upKeys = ['question', 'exclam', "percent", 
          "dollar", "ampersand", "quotedbl", "apostrophe", 
          "parenleft", "parenright", "asterisk", "equal", 
          "slash", "colon", "semicolon", "greater", "underscore"
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
                  

def changeTimer(): 
    SurfThread.timer = True
        
