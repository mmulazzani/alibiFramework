#! /bin/env python
# -*- coding: utf-8 -*-
'''
Created on 27.02.2013

@author: steffi
'''

import threading
import time
import emailResponder, sys
from emailResponder import EmailResponder
from chatResponder import ChatResponder

class ServerStarter(threading.Thread):

    def run(self):
        email  = EmailResponder()
        email.start()
        
        skype = ChatResponder()
        skype.start()
        # TIMER anpassen
        time.sleep(1900)
        emailResponder.changeTimer()
        chatResponder.shutdown()
        sys.exit(0)
        
ServerStarter().start()
    
    
    
    
