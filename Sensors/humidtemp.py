#!/usr/bin/python
import json
import time
import requests
import board
import busio
import adafruit_am2320

# create the I2C shared bus
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_am2320.AM2320(i2c)


def posthumidity(value):
    print("Posting humidity to API")

    url = 'http://192.168.43.4:8090/sensors/'
    payload = {
        'type': 'humidity',
        'value': value
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)


def posttemp(value):
    print("Posting temp to API")

    url = 'http://192.168.43.4:8090/sensors/'
    payload = {
        'type': 'temp',
        'value': value
    }
    headers = {'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    print(response.text)


starttime = time.time()
while True:
    print("Temperature: ", sensor.temperature)
    print("Humidity: ", sensor.relative_humidity)

    posthumidity(sensor.relative_humidity)
    posttemp(sensor.temperature)

    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
