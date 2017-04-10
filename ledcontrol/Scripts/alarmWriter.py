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

##########################################################################
######### Generating a string in the format of the alarms.save ###########
def writeAlarms(alarms):
    ausgabe = tupela(alarms)
    isList = True
    counter = 0
    for alarm in alarms:
        ausgabe += tupeli(str(counter), alarms)
        ausgabe += tupelstr('year') + tupelstr1(alarms[counter].get('year'),True)
        ausgabe += tupelstr('month') + tupelstr1(alarms[counter].get('month'),True)
        ausgabe += tupelstr('day') +tupelstr1(alarms[counter].get('day'),True)
        ausgabe += tupelstr('hour') + tupelstr1(alarms[counter].get('hour'),True)
        ausgabe += tupelstr('minute') + tupelstr1(alarms[counter].get('minute'),True)
        ausgabe += tupelstr('duration') + tupelstr(alarms[counter].get('duration'))
        ausgabe += tupelstr('cutoff') + tupelstr(alarms[counter].get('cutoff'))
        ausgabe += tupelstr('monday') + tupelstr(alarms[counter].get('monday'))
        ausgabe += tupelstr('tuesday') + tupelstr(alarms[counter].get('tuesday'))
        ausgabe += tupelstr('wednesday') + tupelstr(alarms[counter].get('wednesday'))
        ausgabe += tupelstr('thursday') + tupelstr(alarms[counter].get('thursday'))
        ausgabe += tupelstr('friday') + tupelstr(alarms[counter].get('friday'))
        ausgabe += tupelstr('saturday') + tupelstr(alarms[counter].get('saturday'))
        ausgabe += tupelstr('sunday') + tupelstr(alarms[counter].get('sunday'))
        ausgabe += "}"
        counter += 1
    ausgabe += "}"

    target = open('alarms.save', 'w')
    target.write(ausgabe)
    target.close()


##############################################################################
#################### Functions for the repeating tupels ######################
def tupela(a):
    return ("a:" + str(len(a)) + ":{")
def tupels(s):
    return ("s:" + str(len(s)) + ":")
def tupeli(i, a):
    return ("i:" + i + ";" + tupela("12345678901234"))
def tupelstr(s):
    return ("s:" + str(len(s)) + ":\"" + s + "\";")
def tupelstr1(s,t):
    if(t and len(s)<2):
        s = "0"+ s
    return ("s:" + str(len(s)) + ":\"" + s + "\";")
