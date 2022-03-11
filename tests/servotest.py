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
time.sleep(1)
while True:
    kit.servo[0].angle = 40
#    time.sleep(0.1)
    kit.servo[1].angle = 140
#    time.sleep(0.1)
    kit.servo[2].angle = 40
#    time.sleep(0.1)
    kit.servo[3].angle = 140
    time.sleep(1.5)
    kit.servo[0].angle = 120
#    time.sleep(0.1)
    kit.servo[1].angle = 60
#    time.sleep(0.1)
    kit.servo[2].angle = 140
#    time.sleep(0.1)
    kit.servo[3].angle = 40
    time.sleep(1.5)
