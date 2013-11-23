# -*- coding: utf-8 -*-
'''
Created on 27.02.2013

@author: steffi
'''

import threading
import time, subprocess, Skype4Py, aiml, random

class ChatResponder(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        print "skype starten"
        ChatResponder.skype = Skype4Py.Skype()
        ChatResponder.skype.OnMessageStatus = OnMessageStatus
        ChatResponder.skype.Attach()
        time.sleep(3)
        subprocess.call(["xte", "key Return"])
        
        ChatResponder.k = aiml.Kernel()
        ChatResponder.k.learn("std-startup.xml")
        ChatResponder.k.respond("load aiml b")
    	time.sleep(random.randint(2,30))
	# namen anpassen!
    	ChatResponder.skype.CreateChatWith("TODO").SendMessage("hey, what's up?")
        time.sleep(random.randint(2,30))
        ChatResponder.skype.CreateChatWith("TODO").SendMessage("how are you?")
    	time.sleep(random.randint(2,30))
    	ChatResponder.skype.CreateChatWith("TODO").SendMessage("what are you doing today? i want to go swimming")


def OnMessageStatus(Message, Status):
    if Status == 'RECEIVED':
        print(Message.FromDisplayName + ': ' + Message.Body)  
        __sendMessageBack(Message.Sender.Handle, Message.Body)

def __sendMessageBack(name, message):
    time.sleep(random.randint(2,120))
    #namen anpassen!!
    if name == "TODO" or name == "TODO" or name == "TODO" or name == "TODO":
        if ChatResponder.timer == False:
            randChoose = random.randint(0,10)
            if randChoose == 5 or randChoose == 7 or len(message) > 50:
                randIndex = random.randint(0, len(messages)-1)
		messageToSend = messages[randIndex]
		time.sleep(len(messageToSend)*0.1)
                ChatResponder.skype.CreateChatWith(name).SendMessage(messageToSend)
            else:
                messageToSend = ChatResponder.k.respond(message)
		time.sleep(len(messageToSend)*0.1)
	        ChatResponder.skype.CreateChatWith(name).SendMessage(messageToSend)
        else:
            messageToSend = "I have to go, see you, byebye"
            ChatResponder.skype.CreateChatWith(name).SendMessage(messageToSend)   
            ChatResponder.skype = None
        

messages = ["how long do you stay in Canada?", "do you believe in god?", "do you like star wars?", "my favourite food is sushi",
"what is your age?", "tell me a secret", "do you like me?", "i  like your beautiful eyes", "you are embarrasing me!", 
"what are your plans for today?", "do you want to go to cinema tonight?", "how is it going with your master thesis?",
"do you go on holiday next week?", "do you like the film 'star wars'?", "i am sorry, i did not understand you", 
"how many times did we discuss about this topic?", "nice :-)", ":-D","ok", "what?", "i am very tired", "do you have a cold?",
 "you should drink more tea!", "not so good :-/", "oh ok :-(", "ok", "well, i don't think so!", "what do you know about alaska?"]

def shutdown():
    print "shutdown SKYPE - ausbaubar"
    ChatResponder.timer = True

ChatResponder.skype = None
ChatResponder.k = None
ChatResponder.timer = False
