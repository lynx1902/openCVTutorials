import cv2

img = cv2.imread('lena.jpg',-1)# imread func with 0,1,-1 for colored gray and alpha channels
print(img)
cv2.imshow('image',img)# displays the img
k = cv2.waitKey(0) &0xFF #displays screen infintely until keypress
if k==27:# value for escape key
    cv2.destroyAllWindows()#close all windows
elif k == ord('s'):# if key s is pressed 
    cv2.imwrite('lena_copy.png',img)# writes og img into a copy 
    cv2.destroyAllWindows() #close all windows
       