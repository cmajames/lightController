import RPi.GPIO as GPIO

red = 26
blue = 20
green = 21

GPIO.setmode(GPIO.BCM)

keys = dict(
	key = "",
	key_secret = "",
	token = "",
	token_secret = "",
)

colors = dict(
	red = "red",
	blue = "blue",
	green = "green",
	orange = "orange",
	yellow = "yellow",
	purple = "purple",
	white = "white",
	black = "black"
)


def coloroutput(i):
	if(i == "red"):
		GPIO.output(red, True)
		GPIO.output(green, False)
		GPIO.output(blue, False)

	if(i == "blue"):
		GPIO.output(red, False)
		GPIO.output(green, False)
		GPIO.output(blue, True)

	if(i == "green"):
		GPIO.output(red, False)
		GPIO.output(green, True)
		GPIO.output(blue, False)

	if(i == "orange"):
		GPIO.output(red, True)
		GPIO.output(green, True)
		GPIO.output(blue, False)

	if(i == "yellow"):
		GPIO.output(red, False)
		GPIO.output(green, True)
		GPIO.output(blue, True)

	if(i == "purple"):
		GPIO.output(red, True)
		GPIO.output(green, False)
		GPIO.output(blue, True)

	if(i == "white"):
		GPIO.output(red, True)
		GPIO.output(green, True)
		GPIO.output(blue, True)

	if(i == "black"):
		GPIO.output(red, False)
		GPIO.output(green, False)
		GPIO.output(blue, False)

