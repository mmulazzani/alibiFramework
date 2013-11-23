# -*- coding: utf-8 -*-
'''
Created on 27.02.2013

@author: steffi
'''
import threading
import poplib, smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import time, random

class EmailResponder(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self) 
	#daten anpassen
        self.gmail_user = "" # emailadresse (gmail)
        self.gmail_pwd = "" # password
        self.emailcount = 0
        EmailResponder.timer = False
    
    def run(self):
        while EmailResponder.timer == False:
            print "check emails"
            if self.newEmails() == True:
                time.sleep(random.randint(1,300))
                self.respondEmails()
            time.sleep(30)
        print "emailserver beendet"

    def newEmails(self):
        pop_conn = poplib.POP3_SSL('pop.gmail.com')
        pop_conn.user(self.gmail_user)
        pop_conn.pass_(self.gmail_pwd)
        
        emailcount_new = len(pop_conn.list())
        print "count alt = " + str(self.emailcount) + " count neu = " + str(emailcount_new)
        
        if emailcount_new > self.emailcount:
            print "neues email angekommen"
            self.emailcount = emailcount_new
            pop_conn.quit()
            return True
        else:
            print "keine neuen emails angekommen"
            self.emailcount = emailcount_new
            pop_conn.quit()
            return False
       
    
    
    def respondEmails(self):
        print "respond email"
        rand = random.randint(0,(len(topic)-1))        
	# emailadresse anpassen, an empfängger
        self.__mail("TODO", topic[rand], text[rand])

    def __mail(self, to, subject, text):
        msg = MIMEMultipart()
        
        msg['From'] = self.gmail_user
        msg['To'] = to
        msg['Subject'] = subject
         
        msg.attach(MIMEText(text))
        
        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(self.gmail_user, self.gmail_pwd)
        mailServer.sendmail(self.gmail_user, to, msg.as_string())
        # Should be mailServer.quit(), but that crashes...
        mailServer.close()
        
        
        
topic = ['Einkaufen', 'Kino Morgen' , 'Umfrage', 'Uni-Zeug', 'Strandbad', 'Urlaub']

text = ['Hallo,\nwir haben ja ausgemacht, dass wir einkaufen gehen. \nwann hast du denn zeit \n lg', 'Hallo \nhast du Lust morgen ins Kino zu gehen? ich mag gern den spannenden film sehen, den wir letztens in der vorschau gesehen haben. was meinst du? \nlg margit', 'Hallo, \nkannst du an der Umfrage wegen der Diplomarbeit teilnehmen? ich hab dir die Unterlagen mitgeschickt. Es ist wirklich wichtig! danke dir! \nlg m', 'Hallo, \nich wollte dich nur noch einmal erinnern, dass wir bis zum Ende des Monats die Aufgabe mit den Verteilten Systemen fertig stellen sollten. Hast du schon angefangen? ich leider noch nicht, werd mich aber bald dazu setzen. meld dich, wenn du beginnst, dann tauschen wir uns aus, wie es uns gegangen ist. \nbis bald und lg m', 'hallo \ngehst du heute strandbad? bin ws nach der arbeit ab 15 uhr dort. \nlg margit', 'guten morgen\n ich wollte nur kurz fragen, wie es bei euch in der urlaubszeit ausschaut, wann ihr zeit habt und ob ihr schon was geplant habts. ich fahre wahrscheinlich nach Italien und freu mich auf Gesellschaft! \nlg']
        
def changeTimer():
    EmailResponder.timer = True
