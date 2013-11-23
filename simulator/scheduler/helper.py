# -*- coding: utf-8 -*-
'''
Created on 21.02.2013

@author: steffi
'''


import os, subprocess
import time
import random
import constants
import documentsThread, calculatorThread, skypeThread, surfThread, thunderbirdThread 
import textThread, vlcThread, gameThread

myThreads = []
breite = constants.BREITE
hoehe = constants.HOEHE
_format = constants.FORMAT

def startThunderbird():
    try:       
 # alle thunderbird randomlogik hier
        rand = random.randrange(0,4)
        thb = thunderbirdThread.ThunderbirdThread()
        thb.start()
        time.sleep(7)
        
        time.sleep(rand + 3)
        thb.readNewMessages()
        time.sleep(rand+2)
        if rand == 0:
            thb.writeEmail()
        elif rand == 1:
            thb.respondEmail()
        elif rand == 2:
            thb.fowardEmail()
        elif rand == 3:
            thb.deleteEmail()
        #randombeenden von thunderbird
        
        if rand != 0:
            thb.closeThunderbird()
    
    except Exception as e:
        print e
        pass
        
def startAnyProgram():
    try:
        rand = random.randrange(1,4)
        if rand == 1:
            print "calc"
            calculator = calculatorThread.CalculatorThread()
            time.sleep(3)
            calculator.start()
            calculator.calculate()
        if rand == 2:
            print "game"
            game = gameThread.GameThread(random.randrange(0,4))
            game.start()
            time.sleep(random.randrange(20,30))
            game.closeGame()
	    if rand == 3:
 	        print "video"
	        video = vlcThread.VLCThread()
	        video.start()            
            if rand == 4:
                print "data"
                txtNr = random.randrange(0,3)
                textThread.editDocuments(txtNr)
    except Exception as e:
	    print e	   
  	    pass

def startDocuments():
    try:
        doc = random.randrange(0,1)
        if doc == 0:
            libre = documentsThread.DocumentsThread()
            libre.start()  
            time.sleep(5)
            libre.startLibreOfficeSimulation(30)
        else: 
            documentsThread.openAndClosePdf()
           
    except Exception as e:
        print e	   
        pass
  
def startSurfing():
	try:
            surfen = surfThread.SurfThread(hoehe, breite, _format)
            surfen.starte()
	except Exception as e:
	    print e
	    pass
        
def startSkype():
    try:
   	 skype = skypeThread.SkypeThread()
   	 skype.start()
   	 myThreads.append(skypeThread)
    except Exception as e:
	print e
	pass

def shutdown():
    print "shutdown: helper"
    thb = thunderbirdThread.ThunderbirdThread()
    thb.start()
    thb.shutdown()
    
    surfThread.timer = True
    print "timer surfen:"+str(surfThread.timer)
    
    for th in myThreads:
        th.shutdown() 
        time.sleep(5)
        



    
    
