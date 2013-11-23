'''
Created on 21.02.2013

@author: steffi
'''
import time
import Skype4Py
import subprocess
import aiml, threading, random

class SkypeThread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        print "skype startennnn"
        SkypeThread.skype = Skype4Py.Skype()
        SkypeThread.skype.OnMessageStatus = OnMessageStatus
        SkypeThread.skype.Attach()
        time.sleep(3)
        subprocess.call(["xte", "key Return"])
        #logger.log("skype gestartet")
        
        
        SkypeThread.k = aiml.Kernel()
        SkypeThread.k.learn("/home/steffi/Programme/scheduler/std-startup.xml")
        SkypeThread.k.respond("load aiml b")
        print "skype startup complete"

def OnMessageStatus(Message, Status):
    if Status == 'RECEIVED':
        print(Message.FromDisplayName + ': ' + Message.Body)
	__sendMessageBack(Message.Sender.Handle, Message.Body)
        
def __sendMessageBack(name, message):
    print "response"
    if SkypeThread.timer == False:
	time.sleep(random.randint(15,120))
        responseMessage = SkypeThread.k.respond(message)
        time.sleep(len(responseMessage)*0.1)
        SkypeThread.skype.CreateChatWith(name).SendMessage(responseMessage)
    else: 
        messageToSend = "Sorry, I have to go! Bye!"
	time.sleep(random.randint(15,30))
        SkypeThread.skype.CreateChatWith(name).SendMessage(messageToSend)        
        SkypeThread.skype = None
    
        
def shutdown():
    print "shutdown SKYPE"
    SkypeThread.timer = True
    __sendMessageBack("steffi.spam", "bye")
    SkypeThread.skype = None

SkypeThread.skype = None
SkypeThread.k = None
SkypeThread.timer = False
