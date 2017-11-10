#
# Generating a string in the format of the alarms.save


def write_alarms(alarms):
    ret = tuple_a(alarms)
    counter = 0
    for alarm in alarms:
        ret += tuple_i(str(counter))
        ret += tuple_str('year') + tuple_str1(alarms[counter].get('year'))
        ret += tuple_str('month') + tuple_str1(alarms[counter].get('month'))
        ret += tuple_str('day') + tuple_str1(alarms[counter].get('day'))
        ret += tuple_str('hour') + tuple_str1(alarms[counter].get('hour'))
        ret += tuple_str('minute') + tuple_str1(alarms[counter].get('minute'))
        ret += tuple_str('duration') + tuple_str1(alarms[counter].get('duration'))
        ret += tuple_str('cutoff') + tuple_str1(alarms[counter].get('cutoff'))
        ret += tuple_str('monday') + tuple_str1(alarms[counter].get('monday'))
        ret += tuple_str('tuesday') + tuple_str1(alarms[counter].get('tuesday'))
        ret += tuple_str('wednesday') + tuple_str1(alarms[counter].get('wednesday'))
        ret += tuple_str('thursday') + tuple_str1(alarms[counter].get('thursday'))
        ret += tuple_str('friday') + tuple_str1(alarms[counter].get('friday'))
        ret += tuple_str('saturday') + tuple_str1(alarms[counter].get('saturday'))
        ret += tuple_str('sunday') + tuple_str1(alarms[counter].get('sunday'))
        ret += "}"
        counter += 1
    ret += "}"

    target = open('alarms.save', 'w')
    target.write(ret)
    target.close()


# Functions for the repeating tuples
def tuple_a(a):
    return "a:" + str(len(a)) + ":{"


def tuple_s(s):
    return "s:" + str(len(s)) + ":"


def tuple_i(i):
    return "i:" + i + ";" + tuple_a("12345678901234")


def tuple_str(s):
    return "s:" + str(len(s)) + ":\"" + s + "\";"


def tuple_str1(s):
    if len(s) < 2:
        s = "0" + s
    return "s:" + str(len(s)) + ":\"" + s + "\";"
