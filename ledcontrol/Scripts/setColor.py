import time
from Scripts.pinparser import parse_pins
import sys

# import tty
# import pigpio

pins = parse_pins()
RED_PIN = pins[0]
GREEN_PIN = pins[1]
BLUE_PIN = pins[2]

try:
    r = int(sys.argv[1])
    g = int(sys.argv[2])
    b = int(sys.argv[3])
except Exception:
    r = 17
    g = 22
    b = 24


# pi = pigpio.pi()


def set_lights(pin, brightness, smooth):
    if smooth:
        actual_brightness = 20 #int(pi.get_PWM_dutycycle(pin))
        val = float(brightness - actual_brightness)
        val = float(1 / val)
        while actual_brightness < brightness:
            actual_brightness += 1
            # pi.set_PWM_dutycycle(pin, actual_brightness)
            time.sleep(val)
        # pi.set_PWM_dutycycle(pin, brightness)
    else:
        b = 0
        #pi.set_PWM_dutycycle(pin, brightness)


set_lights(RED_PIN, r, True)
set_lights(GREEN_PIN, g, True)
set_lights(BLUE_PIN, b, True)

# pi.stop()
