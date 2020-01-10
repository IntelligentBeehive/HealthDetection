import sys
import os
sys.path.insert(1, 'BroodPatternAI/')
sys.path.insert(2, 'PopulationCounter/')

from Classifier import *
from BeeCounter import *
import keyboard
import time

print("******Starting health Detection******")
print("please enter the ->")
sleepTime = input("please enter the amount of time the program needs to wait before a new detection cycle. A value of 21600 is recommended since this makes 4 detections each day->") 


while True:

    print("Making image from camera")
    
    dirname = os.path.dirname(__file__)
    brood_pattern_file = os.path.join(dirname, "BroodPatternAI/DataSetV1/Test/b2.jpg")
    hive_file = os.path.join(dirname,"PopulationCounter/kast1.jpeg")

    img = cv2.imread(hive_file)

    print("classifying brood pattern image")
    results = Classify(brood_pattern_file)

    print(results)

    print("Counting bees")
    beeCount = run(img)

    print(beeCount)

    time.sleep(int(sleepTime))



    