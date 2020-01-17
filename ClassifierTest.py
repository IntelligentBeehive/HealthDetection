import sys
sys.path.insert(1, 'BroodPatternAI/')
sys.path.insert(2, 'PopulationCounter/')

from Classifier import *
from BeeCounterDEMO import *
  
img = cv2.imread("BroodPatternAI/DataSetV1/Test/h6.jpg")
results = Classify("BroodPatternAI/DataSetV1/Test/h6.jpg")  

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
