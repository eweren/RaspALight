import os
import sys
import datetime
import time
from Scripts.pinparser import parse_pins
from Scripts.setColor import set_lights
from Scripts.alarmParser import parse_alarms
from Scripts.alarm import alarm

# import tty
# import pigpio

# Standard config.
pins = parse_pins()
RED_PIN = int(pins[0])
GREEN_PIN = int(pins[1])
BLUE_PIN = int(pins[2])

# Get the custom pin numbers.
with open('settings.save') as f:
    file = [line.rstrip('\n') for line in f]
for x in file:
    settings = x.split(",")
    RED_PIN = settings[0]
    GREEN_PIN = settings[1]
    BLUE_PIN = settings[2]

STEPS = 1

bright = 0.00
r = 0.00
g = 0.00
b = 0.00


# Wait until the alarm has to start. Trigger the light up def
def wait(old_timeobj, duration, co):
    print("Next Alarm: ", old_timeobj, " - ", duration)
    while datetime.datetime.now() < old_timeobj:
        time.sleep(5)
    if light_up(int(duration), old_timeobj):
        cut_off(co, old_timeobj)
    return False


# Slowly lighten up based on the duration.
# Return True, if it ran through and False if the alarm was cancelled.
def light_up(duration, old_timeobj):
    abort = False
    hops = float(duration) * 60 / 255 * STEPS
    print("Dimmen beginnt!")
    d = datetime.datetime.now()
    print("Uhrzeit:", d.time())
    # var for setting g one up every seventh time of r
    i = 0
    global r
    r = 0.0
    global g
    g = 0.0
    global bright
    bright = 0
    while bright < 255 and not abort:
        print(bright)
        with open('abort.save', 'r') as f:
            content = f.read()
        for letter in content:
            if letter == "1":
                target = open('abort.save', 'w')
                target.write("0")
                target.close()
                return False
        i = i + 1
        time.sleep(hops)
        r = r + 1
        set_lights(RED_PIN, r, False)
        if i % 7 == 0:
            g = g + 1
            set_lights(GREEN_PIN, g, False)
        bright = bright + STEPS
    d = datetime.datetime.now()
    print("Uhrzeit:", d.time())
    return True


# Slowly lighten down based on the cutoff time
def cut_off(co, old_timeobj):
    global r
    global b
    hops = float(co)
    bright = 255;
    while bright > 0:
        time.sleep(hops * 60 / 255 * STEPS)
        set_lights(RED_PIN, r, False)
        set_lights(GREEN_PIN, g, False)
        bright = bright - STEPS


# time.sleep(0.5)

# pi.stop()
