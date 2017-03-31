###### CONFIGURE THIS ######

# The Pins. Use Broadcom numbers.
FILE = open("/var/www/html/ledcontrol/Scripts/pins.save", "r")
VARIABLES = FILE.read()
RED_PIN,GREEN_PIN,BLUE_PIN,CUT_OFF_TIME = VARIABLES.split(",")
RED_PIN = int(RED_PIN)
GREEN_PIN = int(GREEN_PIN)
BLUE_PIN = int(BLUE_PIN)
CUT_OFF_TIME = int(CUT_OFF_TIME)
print (RED_PIN)
print(BLUE_PIN)
print(GREEN_PIN)
print(CUT_OFF_TIME)
# Number of brightness change per step (more is faster, less is slower).

# You also can use 0.X floats.

STEPS     = 0.01

###### END ######

import os

import sys

import termios

import tty

import pigpio

import time

import datetime

from thread import start_new_thread

yop = sys.argv[1]

mop = sys.argv[2]

dp = sys.argv[3]

hp = sys.argv[4]

mp = sys.argv[5]

duration =sys.argv[6]

startzeit=datetime.datetime(2000, 1, 1, 1, 1, 1)

jetzt = datetime.datetime.now()

hint = int(hp) - 1
mint = int(mp)
durationint = int(duration)
_TIME_ALARM = datetime.datetime(int(yop),int(mop),int(dp),int(hp),int(mp))
__TIMEDELTA_DURATION = datetime.timedelta(minutes = int(duration))
startzeit = _TIME_ALARM - __TIMEDELTA_DURATION


print "Wecker Startzeit"
print startzeit

bright = 0.00

r = 255.00

g = 35.00

b = 0.00



brightChanged = False

abort = False

state = True

pi = pigpio.pi()

def updateColor(color, step):

        color += step


        if color > 255:

                return 255

        if color < 0:

                return 0



        return color
def setLights(pin, brightness):

        realBrightness = int(int(brightness) * (float(bright) / 255.0))

        pi.set_PWM_dutycycle(pin, realBrightness)





def getCh():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
                tty.setraw(fd)
                ch = sys.stdin.read(1)
        finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def checkKey():
        global bright
        global brightChanged
        global state
        global abort
        while True:                c = getCh()
                if c == 'c' and not abort:
                        abort = True
                        break

start_new_thread(checkKey, ())

print ("c = Wecker abbrechen")


def cut_off():
    cutofftime
    while  cutofftime > 0:
            time.sleep(60)
            CUT_OFF_TIME = CUT_OFF_TIME - 1;
    abort = true;


setLights(RED_PIN, r)

setLights(GREEN_PIN, g)

setLights(BLUE_PIN, b)

while abort == False:
        hops = float(durationint)
        if state and not brightChanged:

                if bright < 255:
                        while  datetime.datetime.now() < startzeit:
                                time.sleep(10)

                        brightChanged = True
                        time.sleep(hops * 60 / 255 * STEPS)
                        brightChanged = False
                        setLights(RED_PIN, r)
                        setLights(GREEN_PIN, g)

                        bright = bright + STEPS

                elif bright >= 255:
                        print("Alarm finished")
                        while  CUT_OFF_TIME > 0:
                                CUT_OFF_TIME = CUT_OFF_TIME - 1;
                                time.sleep(60)
                        abort = True;
print ("Aborting...")
setLights(RED_PIN, 0)

setLights(GREEN_PIN, 0)

setLights(BLUE_PIN, 0)
time.sleep(0.5)

pi.stop()
