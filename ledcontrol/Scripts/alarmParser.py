# Works
# Parses the alarms from the save_file


def parse_alarms():
    # Open the file, the alarm are saved
    with open('alarms.save', 'r') as f:
        content = f.read()
    alarms = False
    alarm = False
    opened = False
    key = False
    value = False
    value_str = ""
    key_str = ""
    counter = 0
    alarms_list = list()

    # iterate over and create alarm-objects from all the lines
    for letter in content:
        if letter == "{" and alarms is False:
            alarms = True
        elif letter == "{" and alarms:
            alarm = True
            alarm_dict = dict()

        if letter == "\"" and alarm:
            if opened:
                opened = False
                counter = counter + 1
                if value_str != "":
                    alarm_dict.update({key_str: value_str})
                    key_str = ""
                    value_str = ""

            elif opened is False:
                if counter % 2 == 0:
                    key = True
                    value = False
                else:
                    key = False
                    value = True
                opened = True

        if opened and key and letter != "\"":
            key_str = key_str + letter
        elif opened and value and letter != "\"":
            value_str = value_str + letter

        if letter == "}" and alarms and not alarm:
            alarms = False
        elif letter == "}" and alarm:
            alarm = False
            alarms_list.append(alarm_dict)
    return alarms_list
