import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
a = 0
key = -1

while key == -1:
    isRead, image = cap.read()
    cv2.imshow('window', image)
    isRead2, image2 = cap.read()
    cv2.imshow('window1', image2)
    key = cv2.waitKey(30)
    a += 1
    print(key)
cap.release()