# Works
# Parses the pins from the save_file


def parse_pins():
    # Open the file, the alarm are saved
    with open('pins.save', 'r') as f:
        content = f.read()
    red = ""
    green = ""
    blue = ""
    r_set = False
    g_set = False
    b_set = False
    values_list = list()
    i = 0

    # iterate over and create alarm-objects from all the lines
    for letter in content:
        if letter != ",":
            if not r_set:
                red = red + letter
            if r_set:
                if not g_set:
                    green = green + letter
                if g_set:
                    if not b_set:
                        blue = blue + letter
        elif letter is ",":
            i += 1
            if r_set:
                if not g_set:
                    g_set = True
                    values_list.append(green)
            if not r_set:
                r_set = True
                values_list.append(red)
    b_set = True
    values_list.append(blue)
    return values_list
