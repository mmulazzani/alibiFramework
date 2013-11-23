# -*- coding: utf-8 -*-
#!/usr/bin/env python

'''
Created on 21.02.2013

@author: steffi
'''


import threading
import time
import helper
import random, sys, shutil

class MainProg(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):     
        timer = 1800
        print "TIMER GESTARTET: " + str(timer) 
        time.sleep(timer)
        self.changeTimer()
        print "TIMER AUS"

    def __readData(self):
        # daten einlesen
        pass
        

    def startSimulation(self):
        MainProg.timer = False
        
        
        #countervariablen
        surfenCount = 0
        emailCount = 0
        anyprogramCount = 0
        documentsCount = 0
        
        # skype starten
        print "start skype"
        helper.startSkype()
        time.sleep(10)
        randalt = 10
        while MainProg.timer == False:
            rand = random.randrange(1, 8)
            time.sleep(rand)
            if rand == randalt:
                rand = randalt - 1
               
            if rand == 1 or rand == 6:
                print "start email"
                if emailCount >= 3:
                    print "skip"
                    continue
                
                emailCount = emailCount+1
                try:
                    helper.startThunderbird()
                except Exception as e:
                    print e
                    pass
            elif rand == 2:
                print "start anyprogram"
                if anyprogramCount >= 10:
                    print "skip"
                    continue
                anyprogramCount = anyprogramCount +1
                try:
                    helper.startAnyProgram()
                except Exception as e:
                    print e
                    pass
            elif rand == 3 or rand == 7:
                print "start documents"
                if documentsCount >= 3:
                    print "skip"
                    continue
                documentsCount = documentsCount +1
                try:
                    helper.startDocuments()
                except Exception as e:
                    print e
                    pass
            elif rand == 5 or rand == 4 or rand == 8:
                print "start surfen"
                if documentsCount >= 5:
                    print "skip"
                    continue
                surfenCount = surfenCount+1
                try:
                    helper.startSurfing()
                except Exception as e:
                    print e
                    pass
	        randalt = rand
       
        print "timer aus"
        helper.shutdown()
	print "EXIT"
	sys.exit(0)
        
    def changeTimer(self):
        MainProg.timer = True
        
scheduler = MainProg()
scheduler.start()
scheduler.startSimulation()        


    

  


# systemdaten anpassen (bildschirmgroesse, gegebenenfalls os)  , usernames, pw







# timer aus: programme schliessen: skype
