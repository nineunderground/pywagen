# @Author: Iñaki Rodriguez <inaki>
# @Date:   14-May-2018
# @Project: pywagen
# @Filename: servoRun.py
# @Last modified by:   inaki
# @Last modified time: 14-May-2018
##################
# servo example  #
##################

# Servo tessting...
import pycom
from lib.superservo import Servo
import time

# Disabling hardbeat
pycom.heartbeat(False)
pycom.rgbled(0x0000FF)  # Blue

# Servo settings
SERVO_PIN = 9  # GP pin
FREQUENCY = 50

servo = Servo(SERVO_PIN, FREQUENCY, 10, 20, 30)

print('Starting loop')
# while True:

print('Turn left - Yellow')
servo.turn_left()
time.sleep(1.25)

print('Turn right - Red')
servo.turn_right()
time.sleep(1.25)

servo.stop()
time.sleep(1.25)
pycom.rgbled(0x000000)
