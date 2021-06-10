import cv2

cap = cv2.VideoCapture(0); #captures video from default camera value 0 , for multiple values can be 1,2,3
fourcc = cv2.VideoWriter_fourcc(*'XVID')#displays a code if avi file is not able to be played because of inappropriate codec
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))#saves the video as output.avi
print(cap.isOpened())#if window is able to display video 
while(cap.isOpened()):
    ret , frame = cap.read()#ret obtains boolean value, frame obtains image array vector
    if ret==True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))# prints the window width
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))# prints the window height
        out.write(frame)
        gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)# converts the color output of the camera to gray
        cv2.imshow('frame',gray)#displays gray video window

        if cv2.waitKey(1) & 0xFF == ord('q'):#refreshes window for 1millisecond reading from cap.read(), closes on pressing 'q'
            break
    else:
        break    
cap.release()#closes capturing device
out.release()
cv2.destroyAllWindows()