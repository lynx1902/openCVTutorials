import numpy as np 
import cv2

#img=cv2.imread('lena.jpg',1)
img = np.zeros([512,512,3], np.uint8)
img= cv2.line(img,(0,0),(255,255),(147,96,44),10) #draws a line on the img
img= cv2.arrowedLine(img,(0,255),(255,255),(255,0,0),10) #draws arrowed line on the img

img= cv2.rectangle(img,(384,0),(510,128),(0,0,255),5) #draws a rectangle on the img
font = cv2.FONT_HERSHEY_SIMPLEX #guves a font face
img= cv2.circle(img,(447,63),63,(0,255,0),-1) #draws a circle

img = cv2.putText(img,"OpenCV",(10,500),font,4,(0,255,255),10,cv2.LINE_AA) #puts a text on img

cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()