import cv2
import numpy


def create_window():
    cv2.namedWindow('window_HSV')
    cv2.resizeWindow('window_HSV', 400, 300)
    cv2.createTrackbar('H_up', 'window_HSV', 255, 255, print)
    cv2.createTrackbar('H_down', 'window_HSV', 0, 255, print)
    cv2.createTrackbar('S_up', 'window_HSV', 255, 255, print)
    cv2.createTrackbar('S_down', 'window_HSV', 0, 255, print)
    cv2.createTrackbar('V_up', 'window_HSV', 255, 255, print)
    cv2.createTrackbar('V_down', 'window_HSV', 0, 255, print)


def get_trackbar_pos():
    H_up = cv2.getTrackbarPos('H_up', 'window_HSV')
    S_up = cv2.getTrackbarPos('S_up', 'window_HSV')
    V_up = cv2.getTrackbarPos('V_up', 'window_HSV')
    H_down = cv2.getTrackbarPos('H_down', 'window_HSV')
    S_down = cv2.getTrackbarPos('S_down', 'window_HSV')
    V_down = cv2.getTrackbarPos('V_down', 'window_HSV')
    return H_up, S_up, V_up, H_down, S_down, V_down

def write_HSV_values(filename):
    f = open(filename, 'w')
    f.write(str(H_up))
    f.write(',')
    f.write(str(H_down))
    f.write(',')
    f.write(str(S_up))
    f.write(',')
    f.write(str(S_down))
    f.write(',')
    f.write(str(V_up))
    f.write(',')
    f.write(str(V_down))
    f.close()

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
key = -1

create_window()
while key == -1:
    isRead, image = cap.read()
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    H_up, S_up, V_up, H_down, S_down, V_down = get_trackbar_pos()
    np_HSV_up = numpy.array([H_up, S_up, V_up])
    np_HSV_down = numpy.array([H_down, S_down, V_down])
    mask = cv2.inRange(image_hsv, np_HSV_down, np_HSV_up)
    cv2.imshow('window', image)
    cv2.imshow('window_mask', mask)
    key = cv2.waitKey(20)
cap.release()
write_HSV_values('HSV_red.txt')
