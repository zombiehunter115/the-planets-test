import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,"sun",(50,300),cv2.FONT_HERSHEY_COMPLEX, 2,(255,255,255))
cv2.putText(img,"mercury",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5 ,(255,255,255))
cv2.putText(img,"venus",(150,300),cv2.FONT_HERSHEY_COMPLEX,0.5 ,(255,255,255))
cv2.putText(img,"earth",(200,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))
cv2.putText(img,"mars",(250,300),cv2.FONT_HERSHEY_COMPLEX,0.5 ,(255,255,255))
cv2.putText(img,"jupiter",(300,300),cv2.FONT_HERSHEY_COMPLEX,0.5 ,(255,255,255))
cv2.putText(img,"starun",(350,300),cv2.FONT_HERSHEY_COMPLEX,0.5 ,(255,255,255))
cv2.putText(img,"uranuns",(400,300),cv2.FONT_HERSHEY_COMPLEX,0.5 ,(255,255,255))
cv2.putText(img,"neptune",(450,300),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255,255,255))




cv2.imshow("The Planets",img)

cv2.waitKey(0)