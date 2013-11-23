
'''
Created on 15.02.2013

@author: steffi
'''

import threading
import os
import random
import subprocess
import time
import decimal

class CalculatorThread(threading.Thread):

    def __init__(self): 
        threading.Thread.__init__(self) 
        CalculatorThread.timer = False
    
    def run(self):  
        os.system("/usr/bin/gcalctool")

    def calculate(self):
        #todo wie oft        
        l = []
        for i in range(0, self.__createRandomShort()):
            l.append(self.__createRandom())
            print i
                
        self.__calculateRandom(l)
        self.shutdown()
        
    def __createRandom(self):
        rand = random.randrange(0,999999)
        if self.__createRandomShort() % 2 == 0:
            rand =  decimal.Decimal(rand)/100
        return rand
    
    def __createRandomShort(self):
        rand = random.randrange(2,5)
        return rand
    
    
    def __add(self, *arguments):
        time.sleep(1)
        subprocess.call(["xte", "key Escape"])
        for i in range(0,len(arguments)):
            time.sleep(1)
            self.__typeNumber(str(arguments[i]))
            
            if i != (len(arguments)-1):
                subprocess.call(["xte", "key plus"])
        
        time.sleep(1)
        subprocess.call(["xte", "key Return"]) 
        
    def __subtract(self, *arguments):
        time.sleep(1)
        subprocess.call(["xte", "key Escape"])
        for i in range(0,len(arguments)):
            time.sleep(1)
            self.__typeNumber(str(arguments[i]))
            if i != (len(arguments)-1):
                    subprocess.call(["xte", "key minus"])
        time.sleep(1)
        subprocess.call(["xte", "key Return"]) 
    
    def __multiply(self, *arguments):
        time.sleep(1)
        subprocess.call(["xte", "key Escape"])
        for i in range(0,len(arguments)):
            time.sleep(1)
            self.__typeNumber(str(arguments[i]))
            if i != (len(arguments)-1):
                subprocess.call(["xte", "keydown Shift_L"])
                subprocess.call(["xte", "key asterisk"])
                subprocess.call(["xte", "keyup Shift_L"])
        time.sleep(1)
        subprocess.call(["xte", "key Return"]) 
        
    def __divide(self, *arguments):
        time.sleep(1)
        subprocess.call(["xte", "key Escape"])
        for i in range(0,len(arguments)):
            time.sleep(1)
            self.__typeNumber(str(arguments[i])) 
            if i != (len(arguments)-1):
                subprocess.call(["xte", "keydown Shift_L"])
                subprocess.call(["xte", "key slash"])
                subprocess.call(["xte", "keyup Shift_L"])
        time.sleep(1)
        subprocess.call(["xte", "key Return"]) 
        
        
    def shutdown(self):
        print "beende calculator in 3 sek"
        time.sleep(3)
        subprocess.call(["xte", "keydown Control_L"])
        subprocess.call(["xte", "key q"])
        subprocess.call(["xte", "keyup Control_L"])
        CalculatorThread.timer = True
        
        
    def __calculateRandom(self, arguments):
        time.sleep(1)
        subprocess.call(["xte", "key Escape"])
        for i in range(0,len(arguments)):
            time.sleep(1)
            self.__typeNumber(str(arguments[i])) 
            if i != (len(arguments)-1):
                operator = self.__selectRandomOperator()
                if operator == "plus" or operator == "minus":
                    subprocess.call(["xte", "key "+operator])
                else:
                    subprocess.call(["xte", "keydown Shift_L"])
                    subprocess.call(["xte", "key "+operator])
                    subprocess.call(["xte", "keyup Shift_L"])
        time.sleep(1)
        subprocess.call(["xte", "key Return"]) 
        
    def __typeNumber(self, arg):
        for j in range(0, len(arg)):    
            nr = arg[j]
            if nr == "-":
                nr = "minus"
            if nr == ".":
                nr = "comma"
            subprocess.call(["xte", "key "+nr])
    
    def __selectRandomOperator(self):
        rand = random.randrange(0,10)
        choice = rand % 4
        
        if choice == 0:
            return "plus"
        elif choice == 1:
            return "minus"
        elif choice == 2:
            return "asterisk"
        elif choice == 3:
            return "slash"
        else:
            return "plus"
        
        
        
def changeTimer(): 
    CalculatorThread.timer = True