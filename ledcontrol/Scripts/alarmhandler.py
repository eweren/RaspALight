import os

import sys

import time

import datetime

import Scripts.alarmexec

import subprocess, signal

import sched
import time
import threading
import _thread
from Scripts.alarmexec import wait
from Scripts.alarm import *

from Scripts.alarmParser import parse_alarms

from Scripts.alarmWriter import write_alarms


# list with all the current alarms
alarms = []


class my_thread(threading.Thread):
    def __init__(self, threadID, name, cur_alarm):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.cur_alarm = cur_alarm

    def run(self):
        print("Starting: " + self.name)
        wait(self.cur_alarm.get_start_time(), self.cur_alarm.get_duration(), self.cur_alarm.get_cutoff())


# Sort the alarms by end_time
def sort(a):
    a.sort(key=lambda alarm: alarm.get_id())
    return a


# Uses the parse function to fill the alarm-list
def get_alarms():
    alarms_array = []
    x = parse_alarms()
    for a in x:
        temp_alarm = alarm(a)
        alarms_array.append(temp_alarm)
    return alarms_array


def abort_alarm_thread():
    target = open('abort.save', 'w')
    target.write("1")
    print("Done")
    target.close()


# Handles the alarms. Starts new thread, when old one finished
def handle():
    try:
        alarms = get_alarms()
        sort(alarms)
        write_alarms(alarms)
        if len(alarms) > 0:
            h_alarm = alarms[0]
            thread1 = my_thread(1, "Alarm", h_alarm)
            thread1.start()
            abort = False
            try:
                # Schleife soll durchlaufen werden, bis Thread nicht mehr aktiv ist.
                while not abort:
                    alarms = get_alarms()
                    sort(alarms)
                    # Wenn Thread aktiv und Alarm noch aktuell -> 2 Sekunden vorm nächsten Prüfen warten.
                    if thread1.is_alive() & (h_alarm.get_id() == alarms[0].get_id()):
                        time.sleep(2)
                    # Wenn Thread noch aktiv, der Alarm aber nicht mehr der aktuelleste/aktuell ist, soll der Thread beendet werden.
                    elif thread1.is_alive() & (h_alarm.get_id() != alarms[0].get_id()):
                        if len(alarms) > 1:
                            if h_alarm.get_id() == alarms[1].get_id():
                                print("Neuer Alarm wurde registriert.")
                            else:
                                print("Aktueller Alarm wurde abgebrochen.")
                                abort_alarm_thread()
                        else:
                            print("Aktueller Alarm wurde abgebrochen.")
                            abort_alarm_thread()
                        abort = True
                    # Thread nicht mehr aktiv -> Aufräumen starten.
                    elif not thread1.is_alive():
                        # Deletes the finished alarm, if it has no repetition
                        if h_alarm.has_no_rep():
                            del alarms[0]
                        # If it has repetition, the next alarm will be calculated
                        else:
                            alarms[0].calc_next()
                        # Updated alarms are written to the save file
                        write_alarms(alarms)
                        abort = True

                    print(thread1.is_alive())
            except Exception:
                print("In exception gelandet")
        else:
            print("waiting for new alarms")
            time.sleep(10)
    except Exception:
        print(Exception)


#while True:
#    handle()
# sys.exit()


s = sched.scheduler(time.time, time.sleep)


def print_time(a='default'):
    print("From print_time", time.time(), a)


def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.run()
    print(time.time())
print_some_times()