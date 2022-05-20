import cv2

cap = cv2.VideoCapture('smart_car.mp4')

for number in range (200):
    isRead, image = cap.read()
    print(image.shape)
    image[50, 550:750] = [0, 0, 255]
    image[50:250, 550] = [0, 0, 255]
    image[250, 550:750] = [0, 0, 255]
    image[50:250, 750] = [0, 0, 255]
    cv2.imshow('window', image)
    crop =image[50:250, 550:750]
    cv2.imshow('window2', crop)
    cv2.waitKey(30)
cap.release()