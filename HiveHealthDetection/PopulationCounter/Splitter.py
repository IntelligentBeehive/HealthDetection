import cv2

img = cv2.imread("kast1.jpeg")

splitHeight = round(img.shape[0] / 3)
splitWidth = round(img.shape[2] / 3)


for i in range(3):
    for j in range(3):
        i *= splitHeight
        j *= splitWidth
        print (i and j)
        crop = img[i:i+splitHeight, j:j+splitWidth]
        cv2.imshow('Image', crop)
cv2.waitKey(0) 
