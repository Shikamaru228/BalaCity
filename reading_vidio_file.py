import cv2
cap = cv2.VideoCapture('car.mp4')
for number in range(1000):
       isRead, image =cap.read()
       cv2.imshow('window', image)
       cv2.waitKey(1)
cap.release()