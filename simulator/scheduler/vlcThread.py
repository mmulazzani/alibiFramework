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



class VLCThread(threading.Thread):

    def __init__(self): 
    	threading.Thread.__init__(self) 
    
    def run(self):
        print "vlc"
	time.sleep(random.randrange(2,5))
        vlc_path = '/usr/bin/vlc'
	numb = random.randrange(0,5)
        video_path = paths[numb]
        subprocess.call([vlc_path, video_path, '--play-and-exit'])  

paths = ['/home/steffi/Videos/wiki.mp4', 
	 '/home/steffi/Musik/elvis1.mp3', 
	 '/home/steffi/Musik/longtimecoming.mp3', 
	 '/home/steffi/Musik/lostthatloving.mp3', 
	 '/home/steffi/Musik/lostthatlovingfeeling.mp3']
