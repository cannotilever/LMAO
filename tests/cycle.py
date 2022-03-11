#!/usr/bin/python3
from adafruit_servokit import ServoKit
import time
kit = ServoKit(channels=16)
i=90
kit.servo[0].angle = 90
time.sleep(0.1)
kit.servo[1].angle = 90
time.sleep(.1)
#kit.servo[2].angle = 90
time.sleep(0.1)
#kit.servo[3].angle = 90
while True:
    for i in range(0,101):
        time.sleep(0.05)
        kit.servo[0].angle = 140-i
        kit.servo[1].angle = 40+i
        kit.servo[2].angle = 40+i
        kit.servo[3].angle = 140-i
    for i in range(0,101):
        time.sleep(0.05)
        kit.servo[0].angle = 40+i
        kit.servo[1].angle = 140-i
        kit.servo[2].angle = 140-i
        kit.servo[3].angle = 40+i
