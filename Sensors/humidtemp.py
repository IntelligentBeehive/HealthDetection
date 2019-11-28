#!/usr/bin/python
import json
import time
import requests


# import sys
# import Adafruit_DHT
# while True:
#
#     humidity, temperature = Adafruit_DHT.read_retry(11, 4)
#
#     print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))


def posthumidity(value):
    print("Posting to API")

    url = 'http://192.168.43.4:8090/sensors/'
    payload = {
        'type': 'humidity',
        'value': value
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)


starttime = time.time()
while True:
    posthumidity(99)
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
