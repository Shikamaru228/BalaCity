import cv2
import numpy

cap = cv2.VideoCapture('blue_car.mp4')

Hu, Su, Vu = 140, 225, 225
Hd, Sd, Vd = 120, 0, 0
HSVu =[Hu, Su, Vu]
HSVd =[Hd, Sd, Vd]

for number in range(330):
    isRead, image = cap.read()
    image_HSV = cv2.cvtColor(image, cv2.COLOR_RGB2HSV_FULL)
    cv2.imshow('window', image)
    cv2.waitKey(20)
cap.release()


































cv2.line(image, (0, 120), (639, 120), (255, 0, 0))
    cv2.line(image, (160, 0), (160, 479), (255, 0, 0))
    cv2.line(image, (0, 360), (639, 360), (255, 0, 0))
    cv2.line(image, (480, 0), (480, 479), (255, 0, 0))