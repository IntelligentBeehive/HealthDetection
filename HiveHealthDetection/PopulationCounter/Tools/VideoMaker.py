
##Startup##
import time, sys											
import cv2														


##Detection##	
stop =	 False

out = cv2.VideoWriter('outputq.avi',cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,(749,429))

while not stop:


	img  = cv2.imread("kast1.jpeg",1)
	out.write(img)
	cv2.imshow('Drones video',img)
	print(img.shape[0])
	print(img.shape[1])
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	cv2.waitKey(1)				
			
cv2.destroyAllWindows() 
