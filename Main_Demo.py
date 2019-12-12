import sys
sys.path.insert(1, 'BroodPatternAI/')
sys.path.insert(2, 'PopulationCounter/')

from Classifier import *
from Demo import *
from random import randrange

count = 0

while True:

    beeCount = run()

    if count > 4:
        count = 0

    if count == 0:
        broodimagepath = "/home/sieuwe/Desktop/Projects/Bijenkast/HealthDetection/BroodPatternAI/DataSetV1/Test/h5.jpg"
    
    elif count == 1:
        broodimagepath = "/home/sieuwe/Desktop/Projects/Bijenkast/HealthDetection/BroodPatternAI/DataSetV1/Test/h1.png"
    
    elif count == 2:
        broodimagepath = "/home/sieuwe/Desktop/Projects/Bijenkast/HealthDetection/BroodPatternAI/DataSetV1/Test/b2.jpg"
    
    elif count == 3:
        broodimagepath = "/home/sieuwe/Desktop/Projects/Bijenkast/HealthDetection/BroodPatternAI/DataSetV1/Test/h6.jpg"
    
    elif count == 4:
        broodimagepath = "/home/sieuwe/Desktop/Projects/Bijenkast/HealthDetection/BroodPatternAI/DataSetV1/Test/b6.jpg"
 
    else:
        broodimagepath = "/home/sieuwe/Desktop/Projects/Bijenkast/HealthDetection/BroodPatternAI/DataSetV1/Test/b6.jpg"

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

    img = np.zeros((300,1500,3))

    if healthy > unhealthy:
        #healthy
        cv2.putText(img, "Status: healthy, because brood pattern is 'Healthy'" ,(10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 250, 50),2,cv2.LINE_AA)
        cv2.putText(img, "And beecount: " + str(beeCount) +" is sufficient" ,(10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 250, 50),2,cv2.LINE_AA)

    else:
        #unhealthy
        cv2.putText(img, "Status: maybe unhealthy, because brood pattern is 'Unhealthy'" ,(10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 250, 50),2,cv2.LINE_AA)
        cv2.putText(img, "But beecount: " + str(beeCount) +" is sufficient" ,(10,90), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(255, 250, 50),2,cv2.LINE_AA)

    cv2.imshow("result", img)
    cv2.waitKey(6000)
