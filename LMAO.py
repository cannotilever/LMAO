#Laura Mood Analasys Output
from adafruit_servokit import ServoKit
import time
time.sleep(5)
kit = ServoKit(channels=16)
import requests
import logging
logging.basicConfig(filename='/tmp/weather.log', encoding='utf-8', level=logging.DEBUG, filemode='w', format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
condListGOOD = [1000,1213,1210,1219,1225,1258]
condListMEH = [1003,1135,1153,1006]
condListBAD = [1243,1114,1168,1183,1186,1009,1279,1222,1189]
condListFUCK = [1117,1171,1195,1201,1207,1237,1246,1249,1282,1276,1264,1252]

def CalcMood():
    conditions = requests.get("http://api.weatherapi.com/v1/current.json?key=9023b09ca5c54e429be200829212712&q=Worcester&aqi=yes").json()["current"]
    #mood starts at 100 and gets reduced by conditions
    mood = 100
    knowncond = False
    #define vars from JSON
    logging.debug("{}\n".format(conditions))
    temp = conditions["temp_f"]
    clouds = conditions["cloud"]
    vis = conditions["vis_miles"]
    wind = conditions["wind_mph"]
    code = conditions["condition"]["code"]
    aqi = conditions["air_quality"]["us-epa-index"]
    if temp > 58 and temp < 80:
        logging.info("Temperature is within optimal range.")
    elif temp < 58:
        mood -= (58-temp)*1.1
    elif temp > 80:
        mood -= (temp-80)*1.5
    for cond in condListGOOD:
        if code == cond:
            mood +=15
            knowncond = True
    for cond in condListMEH:
        if code == cond:
            knowncond = True
            mood -= 20
    for cond in condListBAD:
        if code == cond:
            knowncond = True
            mood -= 45
    for cond in condListFUCK:
        if code == cond:
            knowncond = True
            mood -= 70
    if not knowncond:
        logging.warning("Unknown condition: {}".format(code))
        mood -= clouds*0.4 
        mood -= wind*3
        mood -= (10-vis)*2
    mood -= aqi*0.26
    if mood < 0: mood = 0
    if mood > 100: mood = 100
    logging.info("Calculated mood is: {}".format(mood))
    return mood
lasttime=time.time()-3600
while True:
    if time.time()-lasttime > 900:
        mood = CalcMood()
        lasttime = time.time()
        kit.servo[0].angle = 60+mood*.8
        kit.servo[1].angle = 120-mood*.8
        kit.servo[2].angle = 140-mood
        kit.servo[3].angle = 40+mood
    time.sleep(30)
