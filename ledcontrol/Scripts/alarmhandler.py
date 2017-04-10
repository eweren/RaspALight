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

import time

import datetime

import alarmexec

import subprocess, signal

from alarm import *

from alarmParser import parseAlarms

from alarmWriter import writeAlarms

from threading import *

# list with all the current alarms
alarms = []

##########################################################################
############### Sort the alarms by endtime ###############################
def sort(a):
    a.sort(key=lambda alarm: alarm.getIdent())
    return a

#########################################################################
############ Uses the parse function to fill the alarm-list #############
def getAlarms():
    alarms = []
    x = parseAlarms()
    for a in x:
        talarm = alarm(a)
        alarms.append(talarm)
    return alarms

#########################################################################
###### Handles the alarms. Starts new thread, when old one finished #####
def handle():
    alarms = getAlarms()
    sort(alarms)
    writeAlarms(alarms)
    if(len(alarms)>0):
        alarm = alarms[0]
        thread = Thread(target = alarmexec.wait, args = (alarm.getStarttime(), alarm.getDuration(), alarm.getCutoff(), ))
        # Starts the alarms as a new thread
        thread.start()
        # Catches the return statement of the thread -> True if it has
        # been aborted via web, False if it run through
        abort = thread.join()
        alarms = getAlarms()
        # Deletes the finished alarm, if it has no repetition
        if(alarm.hasNoRep() and ((alarm.getEndtime() + datetime.timedelta(minutes = int(alarm.getCutoff()))) < datetime.datetime.now())):
            del alarms[0]
        # If it has repetition, the next alarm will be calculated
        elif((alarm.getEndtime() + datetime.timedelta(minutes = int(alarm.getCutoff()))) < datetime.datetime.now()):
            alarms[0].calcNext()

        # Updated alarms are written to the save file
        writeAlarms(alarms)
    else:
        sys.exit()
    time.sleep(1)

while(True):
    handle()
#sys.exit()
