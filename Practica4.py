import cv2
import numpy as np
imagen = 0*np.ones((600,600,3),dtype=np.uint8)
global texto 

cv2.line(imagen,(0,0),(600,400),(255,10,0),2)
cv2.line(imagen,(0,0),(400,600),(255,20,0),4)
cv2.line(imagen,(0,0),(200,600),(255,30,0),6)
cv2.rectangle(imagen,(300,300),(50,50),(0,255,0),1)
cv2.circle(imagen,(300,300),10,(100,0,255),3)
font = cv2.FONT_HERSHEY_COMPLEX
print("Ingresa texto")
texto = input()
cv2.putText(imagen,texto,(200,250),font,1,(0,255,255),2,cv2.LINE_AA)


cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()