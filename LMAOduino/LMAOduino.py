#Laura Mood Analasys Output
import time
import serial
import requests
import logging
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=.1)
logging.basicConfig(filename='/tmp/weather.log', encoding='utf-8', level=logging.DEBUG, filemode='w', format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
condListGOOD = [1000,1213,1210,1219,1225,1258,1003]
condListMEH = [1135,1153,1006,1009,1183,1117]
condListBAD = [1243,1114,1168,1186,1279,1222,1189,1195]
condListFUCK = [1171,1201,1207,1237,1246,1249,1282,1276,1264,1252]

def CalcMood():
    conditions = requests.get("http://api.weatherapi.com/v1/current.json?key=9023b09ca5c54e429be200829212712&q=Worcester&aqi=yes").json()["current"]
    #mood starts at 100 and gets reduced by conditions
    mood = 100
    knowncond = False
    #define vars from JSON
    logging.debug("{}\n".format(conditions))
    temp = conditions["temp_f"]
    day = conditions["is_day"]
    clouds = conditions["cloud"]
    vis = conditions["vis_miles"]
    wind = conditions["wind_mph"]
    code = conditions["condition"]["code"]
    aqi = conditions["air_quality"]["us-epa-index"]
    if temp > 58 and temp < 80:
        logging.info("Temperature is within optimal range.")
    elif temp < 58:
        mood -= (58-temp)*0.6
    elif temp > 80:
        mood -= (temp-80)*1.5
    for cond in condListGOOD:
        if code == cond:
            mood += 20
            knowncond = True
    for cond in condListMEH:
        if code == cond:
            knowncond = True
            mood -= 15
    for cond in condListBAD:
        if code == cond:
            knowncond = True
            mood -= 30
    for cond in condListFUCK:
        if code == cond:
            knowncond = True
            mood -= 65
    if not knowncond:
        logging.warning("Unknown condition: {}".format(code))
        mood -= clouds*0.4 
        mood -= wind*3
        if day: mood -= (10-vis)*2
    mood -= aqi*0.26
    if mood < 0: mood = 0
    if mood > 100: mood = 100
    logging.info("Calculated mood is: {}".format(mood))
    return mood
lasttime=time.time()-900
while True:
    if time.time()-lasttime > 900:
        angle = "{}".format(CalcMood())
        lasttime = time.time()
        print(arduino.readline())
        print("Sending ",angle)
        print(type(angle))
        arduino.write(bytes(angle, "utf-8"))
        print("got ",arduino.readline())
        arduino.write(bytes(angle, "utf-8"))
    time.sleep(30)
