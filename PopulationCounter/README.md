Population detection by using:

- 1 A HSV filter to filter out background
- 2 Erode to make mask more dense
- 3 calculate contour of area
- 4 check if area size is sufficent. If this is the case add it to the list of contours
- 5 calculate area of the contours in the list

TODO:
- improve mask on better test images
- transform area into bee count
- split image into a 9 by 9 grid according to the shape of our hive

