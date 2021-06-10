import cv2
import datetime
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

#cap.set(3, 720)#set value of properties
#cap.set(4, 720)
#print(cap.get(3))
#print(cap.get(4))
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: '+str(cap.get(3)) + ' Height: '+ str(cap.get(4))
        datet = str(datetime.datetime.now())    
        frame = cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):#refreshes window for 1millisecond reading from cap.read(), closes on pressing 'q'
            break
        else:
            break  
cap.release()
cv2.destroyAllWindows()     

     