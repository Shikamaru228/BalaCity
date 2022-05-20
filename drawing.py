import cv2

cap = cv2.VideoCapture('robot.mp4')

for number in range(200):
    isRead, image = cap.read()
    cv2.circle(image,(470, 270), 50, (255, 0, 0),3)
    cv2.circle(image, (470, 270), 30, (0, 0, 0), -1)
    cv2.line(image, (480, 45),(480, 495), (255, 0, 255), 5)
    cv2.rectangle(image, (100, 100), (850, 430), (0, 255, 255), 5)
    cv2.putText(image, 'computer vision', (10, 270), cv2.FONT_HERSHEY_SIMPLEX, 3.8, (255, 255, 0), 6)
    cv2.imshow('window', image)
    print(image.shape)
    cv2.waitKey(30)
cap.release()
