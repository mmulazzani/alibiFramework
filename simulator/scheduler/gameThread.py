# -*- coding: utf-8 -*-
'''
Created on 30.04.2013

@author: steffi
'''

import os
import time
import random, subprocess
import threading



class GameThread(threading.Thread):
    
    def __init__(self, rand): 
       threading.Thread.__init__(self) 
       GameThread.gameChooser = rand

    def run(self):
        #choose game
       rand = GameThread.gameChooser
       if rand == 0:
           os.system("/usr/games/mahjongg")
       elif rand == 1:
           os.system("/usr/games/gnomine")
       elif rand == 2:
           os.system("/usr/games/gnome-sudoku")
       elif rand == 3:
           os.system("/usr/games/sol")
       elif rand == 4:
           os.system("/usr/games/sol --freecell")
       
    def closeGame(self):
	if GameThread.gameChooser == 1 or GameThread.gameChooser == 0:
	   key_='q'
        else:
	   key_= 'w'    
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key "+ key_])
        subprocess.call(["xte", "keyup Control_L"])
        time.sleep(2)
    
