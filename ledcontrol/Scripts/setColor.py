###### CONFIGURE THIS ######
# The Pins. Use Broadcom numbers.
RED_PIN   = 22
GREEN_PIN = 24
BLUE_PIN  = 17
###### END ######

import os
import sys
import tty
import pigpio

r = sys.argv[1]
g = sys.argv[2]
b = sys.argv[3]
pi = pigpio.pi()

def setLights(pin, brightness):
        pi.set_PWM_dutycycle(pin, brightness)

setLights(RED_PIN, r)
setLights(GREEN_PIN, g)
setLights(BLUE_PIN, b)

pi.stop()
