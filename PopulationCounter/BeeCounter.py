import cv2
import numpy as np
import time

def detect(img):

    AreaCount = 0

    img_bgr = img
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    #bgd_mask = cv2.inRange(img_hsv, np.array([101, 57, 120]), np.array([108, 103,173])) #Deze werkt goed maar focust veel op reflectie kleur

    bgd_mask = cv2.inRange(img_hsv, np.array([15, 26, 47]), np.array([26, 107, 88])) 
    final_mask = cv2.dilate(bgd_mask, np.ones((5, 5), dtype=np.uint8))

    contours, hierarchy = cv2.findContours(final_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    final_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            final_contours.append(contour)
            AreaCount+=area
    return AreaCount

def run(img):

    TotalAreaCount = 0

    splitHeight = round(img.shape[0] / 3)
    splitWidth = round(img.shape[1] / 3)

    for i in range(3):
        for j in range(3):
            y = i * splitHeight
            x = j * splitWidth
            crop = img[y:y+splitHeight, x:x+splitWidth]
            TotalAreaCount += detect(crop)

    Beecount = round(TotalAreaCount / 102)

    return Beecount
