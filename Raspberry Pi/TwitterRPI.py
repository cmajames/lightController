import time
from tweepy.auth import OAuthHandler
import tweepy
from keysRPI import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = 26
blue = 20
green = 21

GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)


token = keys["token"]
token_secret = keys["token_secret"]
key = keys["key"]
secret = keys["key_secret"] 
auth = OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
client = tweepy.API(auth) 
timeline = client.home_timeline()


def Check():
	def checkfunction():
		for item in timeline:
		    text = "%s says '%s'" % (item.user.screen_name, item.text)
		    for i in colors:
			    if(i in item.text):
			    	coloroutput(i);
			    	print i
			    	return
		print text
	

	checkfunction()

Check()
