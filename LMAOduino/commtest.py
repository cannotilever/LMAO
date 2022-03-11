import serial
import time
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)
while True:
    angle = input("Mood: ")
    print(type(angle))
    arduino.write(bytes(angle, "utf-8"))
    print("got ",arduino.readline())
