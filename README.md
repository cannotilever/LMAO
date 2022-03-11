# Laura Mood Analasys and Output system
(yes the name is a stretch)

## Why does this exist?
This started as I joke with my friend, the titular Laura, that her mood was very weather dependant. I did the reasonable thing and sunk several hours into a physical display of current weather conditions in Worcester, MA in the form of a smiley-face.

## What does it do?
It reads weather data and using highly advanced algorythms *(read: if statments and arbitrary numbers)* outputs to a physical array of servos in the form of a face as pictured below in its full-happy and full-unhappy position.
![image 1](https://github.com/cannotilever/LMAO/raw/main/IMG_0854.JPEG) ![image 2](https://github.com/cannotilever/LMAO/raw/main/IMG_0855.JPEG)
# Why does LMAOduino exist?
I couldn't get my Raspberry Pi to play nice with my school's wifi so I split the functionality into 2 parts:
1) a python script running on a linux laptop that gets weather data over the network and sends it via serial
2) an adruno that actually controls the servos
