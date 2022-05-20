import cv2
import numpy

cap = cv2.VideoCapture(0)

Hu, Su, Vu = 225, 225, 225
Hd, Sd, Vd = 0, 0, 0
HSVu =[Hu, Su, Vu]
HSVd =[Hd, Sd, Vd]
np_u = numpy.array(HSVu)
np_d = numpy.array(HSVd)

for number in range(3000):
    isRead, image = cap.read()
    image_HSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV_FULL)
    mask = cv2.inRange(image_HSV, np_d, np_u)
    cv2.imshow('window2', mask)
    cv2.imshow('window', image)
    cv2.waitKey(20)
cap.release()