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

from alarmParser import *

from alarmWriter import *

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
        thread = Thread(target = alarmexec.wait, args = (alarms[0].getStarttime(), alarms[0].getDuration(), alarms[0].getCutoff(), ))
        # Starts the alarms as a new thread
        thread.start()
        # Gets the ID of the thread
        print("------------------------")
        idt=thread.ident
        print(idt)
        #thread.kill()
        print("------------------------")
        # Ends the thread if finished
        thread.join()
        #ID = sys.argv[1]
        #os.kill(int(ID), signal.SIGKILL)
        print ("thread finished...exiting")
        #start_new_thread(alarmexec.wait(alarms[0].getStarttime(), alarms[0].getDuration(), alarms[0].getCutoff()))
        # Deletes the finished alarm, if it has no repetition
        if(alarms[0].hasNoRep()):
            del alarms[0]
        # If it has repetition, the next alarm will be calculated
        else:
            alarms[0].calcNext()
        # Updated alarms are written to the save file
        writeAlarms(alarms)

#while(True):
handle()
#print("Wait for an alarm")
#time.sleep(10)
