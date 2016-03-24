#!/usr/bin/env python
import feedparser
import time
import RPi.GPIO as GPIO
import imaplib

USERNAME = ""
PASSWORD = ""

obj = imaplib.IMAP4_SSL('imap.gmail.com', '993')
obj.login(USERNAME, PASSWORD)

def markread():
                obj.select('Inbox')
                typ ,data = obj.search(None,'UnSeen')
                obj.store(data[0].replace(' ',','),'+FLAGS','\Seen')


LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
 

while True:
	response = feedparser.parse("https://" + USERNAME + ":" + PASSWORD + "@mail.google.com/gmail/feed/atom")
	unread_count = int(response["feed"]["fullcount"])

	if(unread_count != 0):
		for i in range(0,unread_count):
			#print"(" + str((i+1)) + "/" + str(unread_count) + ")" + response['items'][i].title
			if(response['items'][i].title == 'On' or response['items'][i].title == 'on'):
				#print('On')
				GPIO.output(LED, True)
				markread()
			elif(response['items'][i].title == 'Off' or response['items'][i].title == 'off'):
				#print('Off')
				markread()
				GPIO.output(LED, False)
			else:
				#print('No command found')
				markread()
	else:
                pass
                #print('\n' + 'No unread mail found' + '\n')
        time.sleep(1)
