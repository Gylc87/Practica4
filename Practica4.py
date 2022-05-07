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
print("Ingresa texto: ")
texto = input()
cv2.putText(imagen,texto,(200,250),font,1,(255,255,255),2,cv2.LINE_AA)


img = cv2.imread("img2.jpg")
img = cv2.resize(img, dsize=(550, 350), interpolation=cv2.INTER_CUBIC)
cv2.namedWindow("input image")
cv2.imshow("input image", img)

face = img[50:250, 100:450] 
gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) 
backface = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
img[50:250, 100:450] = backface
cv2.imshow("face", img)
cv2.imshow('imagen',imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()