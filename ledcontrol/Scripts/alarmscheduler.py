import sched
import time
from Scripts.timemaker import *
from Scripts.alarmexec import wait
from Scripts.alarm import *

from Scripts.alarmParser import parse_alarms

from Scripts.alarmWriter import write_alarms

s = sched.scheduler(time.time, time.sleep)


# Uses the parse function to fill the alarm-list


def get_alarm_ids():
    alarms_array = get_alarms()
    x = []
    for a in alarms_array:
        x.append(a.get_id())
    return x

# Uses the parse function to fill the alarm-list
def get_alarms():
    alarms_array = []
    x = parse_alarms()
    for a in x:
        temp_alarm = alarm(a)
        alarms_array.append(temp_alarm)
    return alarms_array


def print_time(a='default'):
    print("From print_time", time.time(), a)


# Sort the alarms by end_time
def sort(a):
    a.sort(key=lambda alarm: alarm.get_id())
    return a


def manage_alarms():
    active_alarms = []
    c = 0
    for alarm in get_alarms():
        alarms = get_alarms()
        print(alarm.get_id(), " - ", alarms[0].get_id())
        time.sleep(3)
        if alarm.get_id() not in active_alarms:
            active_alarms.append(alarm.get_id())
            s.enter(alarm.set_event_id(time.time()), 1, print_time)
            time.sleep(1)
        elif alarm in active_alarms and alarm.get_id() < time.time():
            s.cancel(alarm.get_event_id(), 1, print_time)
    for a in active_alarms:

        alarms = get_alarm_ids()
        if a not in alarms:
            temp_al_ar = get_alarms()
            temp_al_ar.remove(c)
            sort(temp_al_ar)
            write_alarms(temp_al_ar)

        c += 1
    if not s.empty():
        s.run()


while True:
    manage_alarms()
