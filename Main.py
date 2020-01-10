import sys
import os
sys.path.insert(1, 'BroodPatternAI/')
sys.path.insert(2, 'PopulationCounter/')

from Classifier import *
from BeeCounter import *
import time
import requests
import json as js
import datetime

print("******Starting health Detection******")
print("please enter the ->")
sleepTime = input("please enter the amount of time the program needs to wait before a new detection cycle. A value of 21600 is recommended since this makes 4 detections each day->") 


def sendDataToServer(results,beecount,message):

    if results[0][0] == "healthy":
        healthy = round(results[0][1] * 10000) #*10000 because we are leasy and did not wanted to change the api to accept floats
        unhealthy = round(results[1][1] * 10000)
    
    elif results[0][0] == "broodproblem":
        healthy = round(results[1][1] * 10000)
        unhealthy = round(results[0][1] * 10000)

    hiveHealth = round(healthy / 10000 * beecount)

    data = {"beeCount":beecount,
	"broodPatternHealthyConfidence":healthy,
	"broodPatternUnhealthyConfidence":unhealthy,
	"hiveHealth": hiveHealth,
	"message":message}

    r = requests.put(url = "http://145.93.118.99:8090/health/addBeeInfo", data = js.dumps(data), headers = {"Content-Type":"Application/json","Accepts":"Application/json"}) 
    print(r)

def analysePastData():

    currentDate = datetime.date.today() + datetime.timedelta(days=1)
    pastDate = currentDate - datetime.timedelta(days=6)

    message = "http://145.93.118.99:8090/health/getBeeData?timeFrom=" + str(pastDate) + "&timeTo=" + str(currentDate)
    print(message)

    r = requests.get(message)
    data = r.json() 
    
    count = 0
    for i in range(len(data['beeInfo'])):
        count += data['beeInfo'][i]["hiveHealth"]
    
    averageHiveHealth = round(count / len(data['beeInfo']))

    print(averageHiveHealth)

    if averageHiveHealth < 20:
        return "There is a problem with your Hive! Average health: " + str(averageHiveHealth)
    else:
        return "You're Hive is healthy Average health: " + str(averageHiveHealth)
    

while True:

    print("Making image from camera")
    
    dirname = os.path.dirname(__file__)
    brood_pattern_file = os.path.join(dirname, "BroodPatternAI/DataSetV1/Test/b2.jpg")
    hive_file = os.path.join(dirname,"PopulationCounter/kast1.jpeg")

    img = cv2.imread(hive_file)

    print("classifying brood pattern image")
    results = Classify(brood_pattern_file)

    print("Counting bees")
    beeCount = run(img)

    print(beeCount)

    print("Sending data to database")

    message = analysePastData()

    sendDataToServer(results,beeCount, message)

    time.sleep(int(sleepTime))
