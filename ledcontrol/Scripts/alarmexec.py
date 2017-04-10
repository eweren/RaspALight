##########################################################################
#   #######     #######   ###            ######            ##   ######   #
##   #####   #   #####   ##   ###########   ###   #######   #   ####   ###
###   ###   ###   ###   ##   #############   ##            ##   #   ######
####   #   #####   #   ####    ##########   ###   ###   #####      #######
#####     #######     #######    ####   #######   ####   ####   ##   #####
######   #########   ###########     ##########   #####   ###   ####   ###
##########################################################################
import os
import sys
import datetime
import time
#import tty
#import pigpio

###### CONFIGURE THIS ######
# Standard config.
RED_PIN   = 22
GREEN_PIN = 24
BLUE_PIN  = 17

# Get the custon pin numbers.
with open('settings.save') as f: file = [line.rstrip('\n') for line in f]
for x in file:
	settings = x.split(",")
	RED_PIN=settings[0]
	GREEN_PIN = settings[1]
	BLUE_PIN = settings[2]

STEPS     = 1

bright = 0.00
r = 255.00
g = 35.00
b = 0.00

def setLights(pin, brightness):
	x=0
        #realBrightness = int(int(brightness) * (float(bright) / 255.0))

        #pi.set_PWM_dutycycle(pin, realBrightness)

#Wait until the alarm has to start. Trigger the light up def
def wait(timeobj, duration, co):
	print("Next Alarm: ", timeobj)
	while datetime.datetime.now() < timeobj:
		with open('abort.save', 'r') as f:
			file1 = f.read()
			if(file1 is "0"):
				with open('abort.save', 'w') as w:
					w.write("")
				return(True)
		time.sleep(5)
	lightUp(int(duration))
	cutOff(co)
	return(False)

#Slowly lighten up based on the duration.
def lightUp(duration):
	hops = float(duration) * 60
	abort = False
	bright = 0

	while(abort == False):
		if bright < 255:
			time.sleep(hops / 255 * STEPS)
			setLights(RED_PIN, r)
			setLights(GREEN_PIN, g)
			bright = bright + STEPS
			print(bright)
		elif bright >= 255:
			abort=True;

#Slowly lighten down based on the cutoff time
def cutOff(co):
	hops = float(co)
	bright=255;
	while bright>0:
		time.sleep(hops * 60 / 255 * STEPS)
		setLights(RED_PIN, r)
		setLights(GREEN_PIN, g)
		bright = bright - STEPS
		print(bright)

#time.sleep(0.5)

#pi.stop()
