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

def makeTime(alarmarray):
    return datetime.datetime(int(alarmarray.get('year')),int(alarmarray.get('month')),int(alarmarray.get('day')),int(alarmarray.get('hour')),int(alarmarray.get('minute')))

def getStarttime(alarmarray):
    return(getEndtime(alarmarray) - datetime.timedelta(minutes = int(alarmarray.get('duration'))))

def getEndtime(alarmarray):
    return makeTime(alarmarray)

def hasNoRepetition(alarmarray):
    return (int(alarmarray.get('monday')) == 0 & int(alarmarray.get('tuesday')) == 0
    & int(alarmarray.get('wednesday')) == 0 & int(alarmarray.get('thursday')) == 0
    & int(alarmarray.get('friday')) == 0 & int(alarmarray.get('saturday')) == 0
    & int(alarmarray.get('sunday')) == 0)
