import sys
import os
sys.path.insert(1, 'BroodPatternAI/')
sys.path.insert(2, 'PopulationCounter/')

from Classifier import *
from BeeCounterDEMO import *
import time
import requests
import json as js
import datetime

from random import randrange

count = 0

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

    print(data)
    r = requests.put(url = "http://192.168.43.92:8090/health/addBeeInfo", data = js.dumps(data), headers = {"Content-Type":"Application/json","Accepts":"Application/json"}) 
    print(r)
    return data

def analysePastData():

    currentDate = datetime.date.today() + datetime.timedelta(days=1)
    pastDate = currentDate - datetime.timedelta(days=6)

    message = "http://192.168.43.92:8090/health/getBeeData?timeFrom=" + str(pastDate) + "&timeTo=" + str(currentDate)
    print(message)

    r = requests.get(message)
    print(r)
    data = r.json() 
    
    count = 0
    for i in range(len(data['beeInfo'])):
        count += data['beeInfo'][i]["hiveHealth"]
    
    averageHiveHealth = round(count / len(data['beeInfo']))

    #averageHiveHealth = 0
    #if(len(data['beeInfo']) > 0):
    #   averageHiveHealth = data['beeInfo'][len(data['beeInfo'])-1]["hiveHealth"]

    print(averageHiveHealth)

    if averageHiveHealth < 150:
        return "There is a problem with your Hive! Average health: " + str(averageHiveHealth)
    else:
        return "Youre Hive is healthy Average health: " + str(averageHiveHealth)

while True:

    message = analysePastData()

    img = cv2.imread("PopulationCounter/kast1.jpeg")
 
    beeCount = run(img)

    if count > 4:
        count = 0

    if count == 0:
        broodimagepath = "BroodPatternAI/DataSetV1/Test/h5.jpg"
    
    elif count == 1:
        broodimagepath = "BroodPatternAI/DataSetV1/Test/h1.png"
    
    elif count == 2:
        broodimagepath = "BroodPatternAI/DataSetV1/Test/b2.jpg"
    
    elif count == 3:
        broodimagepath = "BroodPatternAI/DataSetV1/Test/h6.jpg"
    
    elif count == 4:
        broodimagepath = "BroodPatternAI/DataSetV1/Test/b6.jpg"
 
    else:
        broodimagepath = "BroodPatternAI/DataSetV1/Test/b6.jpg"

    count += 1

    img = cv2.imread(broodimagepath)
    results = Classify(broodimagepath)

    healthy = 0
    unhealthy = 0

    if results[0][0] == "healthy":
        healthy = round(results[0][1],4)
        unhealthy = round(results[1][1],4)
        print("healthy")
    
    elif results[0][0] == "broodproblem":
        healthy = round(results[1][1],4)
        unhealthy = round(results[0][1],4)
        print("unhealthy")



    cv2.putText(img, "healthy: " + str(healthy) ,(10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 250, 50),2,cv2.LINE_AA)
    cv2.putText(img, "unhealthy: " + str(unhealthy) ,(10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 250, 50),2,cv2.LINE_AA)
    cv2.imshow("result", img)
    cv2.waitKey(6000)

    img = np.zeros((300,1700,3))

    #if healthy > unhealthy:
        #healthy
    #    cv2.putText(img, "Status: healthy, because brood pattern is 'Healthy'" ,(10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 250, 50),2,cv2.LINE_AA)
    #    cv2.putText(img, "And beecount: " + str(beeCount) +" is sufficient" ,(10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 250, 50),2,cv2.LINE_AA)

    #else:
        #unhealthy
    #    cv2.putText(img, "Status: maybe unhealthy, because brood pattern is 'Unhealthy'" ,(10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 250, 50),2,cv2.LINE_AA)
    
    data = sendDataToServer(results,beeCount, message)
    cv2.putText(img, str(data) ,(10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.55,(255, 250, 50),1,cv2.LINE_AA)

    cv2.imshow("result", img)
    cv2.waitKey(6000)
