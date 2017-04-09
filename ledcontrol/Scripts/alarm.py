##########################################################################
#   #######     #######   ###            ######            ##   ######   #
##   #####   #   #####   ##   ###########   ###   #######   #   ####   ###
###   ###   ###   ###   ##   #############   ##            ##   #   ######
####   #   #####   #   ####    ##########   ###   ###   #####      #######
#####     #######     #######    ####   #######   ####   ####   ##   #####
######   #########   ###########     ##########   #####   ###   ####   ###
##########################################################################

import time

import datetime

import time

from timemaker import *

###############################################################################
## Alarm object with vars for start and endtime, as well as its repetition ####
class alarm(object):
    def __init__(self, alarmarray):
        self.duration = alarmarray.get('duration')
        self.cutoff = alarmarray.get('cutoff')
        self.starttime = getStarttime(alarmarray)
        self.endtime = getEndtime(alarmarray)
        self.hasNoRepetition = hasNoRepetition(alarmarray)
        self.repetition = [int(alarmarray.get('monday')),int(alarmarray.get('tuesday')),
        int(alarmarray.get('wednesday')),int(alarmarray.get('thursday')),int(alarmarray.get('friday')),
        int(alarmarray.get('saturday')),int(alarmarray.get('sunday'))]
        self.ident = time.mktime(self.starttime.timetuple())

        #if(not isValid()):
        #   raise ValueError
    def getIdent(self):
        return self.ident

    def getStarttime(self):
        return self.starttime

    def get(self, s):
        if(s=="year"):
            return str(self.endtime.year)
        if(s=="month"):
            return str(self.endtime.month)
        if(s=="day"):
            return str(self.endtime.day)
        if(s=="hour"):
            return str(self.endtime.hour)
        if(s=="minute"):
            return str(self.endtime.minute)
        if(s=="duration"):
            return str(self.duration)
        if(s=="cutoff"):
            return str(self.cutoff)
        if(s=="monday"):
            return str(self.repetition[0])
        if(s=="tuesday"):
            return str(self.repetition[1])
        if(s=="wednesday"):
            return str(self.repetition[2])
        if(s=="thursday"):
            return str(self.repetition[3])
        if(s=="friday"):
            return str(self.repetition[4])
        if(s=="saturday"):
            return str(self.repetition[5])
        if(s=="sunday"):
            return str(self.repetition[6])

    def getEndtime(self):
        return self.endtime

    def getDuration(self):
        return self.duration

    def getCutoff(self):
        return self.cutoff

    def hasNoRep(self):
        return self.hasNoRepetition

###############################################################################
############ Returns the next date, the alarm should be active ################
    def getNextRepetition(self):
        nextDate = -1
        curDay = datetime.date.weekday(self.starttime)
        counter = 0
        # iterate over all the coming repetition days (wednesday to sunday
        # if it is tuesday)
        for item in self.repetition[(curDay + 1):]:
            if item == 1 and nextDate == -1:
                counter += 1
                nextDate = counter
            counter += 1
        #if there was no repetition in the last part of the list,
        # search the rest
        if nextDate == -1 and curDay != -1:
            for item in self.repetition:
                if item == 1 and nextDate == -1:
                    counter += 1
                    nextDate = counter
                counter += 1
        return nextDate

###############################################################################
############# Returns if the alarm is valid or not ############################
    def isValid(self):
        return self.starttime > datetime.datetime.now()

###############################################################################
###################### Calculates the next alarm-time #########################
    def calcNext(self):
        nextDate = self.getNextRepetition()
        self.starttime = self.starttime + datetime.timedelta(days = nextDate)
        self.endtime = self.endtime + datetime.timedelta(days = nextDate)
