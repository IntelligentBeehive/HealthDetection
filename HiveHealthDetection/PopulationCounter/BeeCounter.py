import cv2
import numpy as np
import time

AreaCount = 0

img_bgr = cv2.imread("kast1.jpeg")
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

#bgd_mask = cv2.inRange(img_hsv, np.array([101, 57, 120]), np.array([108, 103,173])) #Deze werkt goed maar focust veel op reflectie kleur

bgd_mask = cv2.inRange(img_hsv, np.array([15, 26, 47]), np.array([26, 107, 88])) 


#final_mask = cv2.erode(bgd_mask, np.ones((3, 3), dtype=np.uint8))
final_mask = cv2.dilate(bgd_mask, np.ones((5, 5), dtype=np.uint8))

cv2.imshow("mask", final_mask)

# Now you can finally find contours.
contours, hierarchy = cv2.findContours(final_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

final_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 300:
        final_contours.append(contour)
        AreaCount+=area


for i in range(len(final_contours)):
    img_bgr = cv2.drawContours(img_bgr, final_contours, i, (50, 250, 50), 4)

cv2.putText(img_bgr,"Total Area: " + str(AreaCount) ,(10,30), cv2.FONT_HERSHEY_SIMPLEX, 1,(50, 250, 50),2,cv2.LINE_AA)

cv2.imshow("result", img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()