from Scripts.timemaker import *


# Alarm object with vars for start and end_time, as well as its repetition
class alarm(object):
    def __init__(self, alarm_array):
        self.duration = alarm_array.get('duration')
        self.cutoff = alarm_array.get('cutoff')
        self.start_time = get_start_time(alarm_array)
        self.end_time = get_end_time(alarm_array)
        self.hasNoRepetition = has_no_rep(alarm_array)
        self.repetition = [int(alarm_array.get('monday')), int(alarm_array.get('tuesday')),
                           int(alarm_array.get('wednesday')), int(alarm_array.get('thursday')),
                           int(alarm_array.get('friday')), int(alarm_array.get('saturday')),
                           int(alarm_array.get('sunday'))]
        self.id = time.mktime(self.start_time.timetuple())
        self.eventid = 0

    def get_id(self):
        return self.id

    def get_start_time(self):
        return self.start_time

    def get(self, s):
        if s == "year":
            return str(self.end_time.year)
        if s == "month":
            return str(self.end_time.month)
        if s == "day":
            return str(self.end_time.day)
        if s == "hour":
            return str(self.end_time.hour)
        if s == "minute":
            return str(self.end_time.minute)
        if s == "duration":
            return str(self.duration)
        if s == "cutoff":
            return str(self.cutoff)
        if s == "monday":
            return str(self.repetition[0])
        if s == "tuesday":
            return str(self.repetition[1])
        if s == "wednesday":
            return str(self.repetition[2])
        if s == "thursday":
            return str(self.repetition[3])
        if s == "friday":
            return str(self.repetition[4])
        if s == "saturday":
            return str(self.repetition[5])
        if s == "sunday":
            return str(self.repetition[6])

    def get_end_time(self):
        return self.end_time

    def get_duration(self):
        return self.duration

    def get_cutoff(self):
        return self.cutoff

    def has_no_rep(self):
        return self.hasNoRepetition

    def set_event_id(self, eid):
        self.eventid = eid - self.get_id()
        return self.get_event_id()

    def get_event_id(self):
        return self.eventid

    # Returns the next date, the alarm should be active
    def get_next_repetition(self):
        next_date = -1
        cur_day = datetime.date.weekday(self.start_time)
        counter = 0
        # iterate over all the coming repetition days (wednesday to sunday
        # if it is tuesday)
        for item in self.repetition[(cur_day + 1):]:
            if item == 1 and next_date == -1:
                counter += 1
                next_date = counter
            counter += 1
        # if there was no repetition in the last part of the list,
        # search the rest
        if next_date == -1 and cur_day != -1:
            for item in self.repetition:
                if item == 1 and next_date == -1:
                    counter += 1
                    next_date = counter
                counter += 1
        return next_date

    # Returns if the alarm is valid or not ------------> Implement that 2 alarm cannot act at the same time.
    def is_valid(self):
        return self.start_time > datetime.datetime.now()

    # Calculates the next alarm-time
    def calc_next(self):
        next_date = self.getNextRepetition()
        self.start_time = self.start_time + datetime.timedelta(days=next_date)
        self.end_time = self.end_time + datetime.timedelta(days=next_date)

    def is_next(self, alarm):
        return self.get_start_time() > alarm.get_start_time()