########################################################################################
#   #######     #######   ###            ######            ##   ######   #            ##
##   #####   #   #####   ##   ###########   ###   #######   #   ####   ###   ###########
###   ###   ###   ###   ##   #############   ##            ##   #   ######           ###
####   #   #####   #   ####    ##########   ###   ###   #####      ###############    ##
#####     #######     #######    ####   #######   ####   ####   ##   ##############    #
######   #########   ###########     ##########   #####   ###   ####   ###             #
########################################################################################

import os

import sys

#########################################################################
################ Parses the alarms from the savefile ####################

def parseAlarms():
    #Open the file, the alarm are saved
    with open('alarms.save', 'r') as f:
       content = f.read()
    alarms = False
    alarm = False
    opened = False
    key = False
    value = False
    valuestr=""
    keystr = ""
    counter = 0
    alarmslist = list()

    #iterate over and create alarm-objects from all the lines
    for letter in content:
        if(letter=="{" and alarms is False):
            alarms = True
        elif(letter=="{" and alarms):
            alarm = True
            alarmdict = dict()

        if(letter=="\"" and alarm):
            if(opened):
                opened=False
                counter = counter + 1
                if(valuestr!=""):
                    alarmdict.update({keystr : valuestr})
                    keystr=""
                    valuestr=""

            elif(opened is False):
                if(counter % 2 == 0):
                    key = True
                    value = False
                else:
                    key = False
                    value= True
                opened = True

        if(opened and key and letter!="\""):
            keystr=keystr + letter
        elif(opened and value and letter!="\""):
            valuestr = valuestr + letter

        if(letter=="}" and alarms and not alarm):
            alarms = False
        elif(letter=="}" and alarm):
            alarm=False
            alarmslist.append(alarmdict)
    return alarmslist
