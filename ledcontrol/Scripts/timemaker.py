import time

import datetime

import time


def make_time(alarm_array):
    return datetime.datetime(int(alarm_array.get('year')), int(alarm_array.get('month')), int(alarm_array.get('day')), int(alarm_array.get('hour')), int(alarm_array.get('minute')))


def get_start_time(alarm_array):
    return get_end_time(alarm_array) - datetime.timedelta(minutes=int(alarm_array.get('duration')))


def get_end_time(alarm_array):
    return make_time(alarm_array)


def has_no_rep(alarm_array):
    return (int(alarm_array.get('monday')) == 0 & int(alarm_array.get('tuesday')) == 0
            & int(alarm_array.get('wednesday')) == 0 & int(alarm_array.get('thursday')) == 0
            & int(alarm_array.get('friday')) == 0 & int(alarm_array.get('saturday')) == 0
            & int(alarm_array.get('sunday')) == 0)
