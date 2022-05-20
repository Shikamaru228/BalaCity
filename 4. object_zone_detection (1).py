import cv2
import numpy
from our_color_functions import get_values_from_file,


def draw_zones(image):
    cv2.line(image, (0, 240), (640, 240), (255, 0, 255), 3)
    cv2.line(image, (320, 0), (320, 480), (255, 0, 255), 3)
    cv2.putText(image, '1', (330, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    cv2.putText(image, '2', (330, 290), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    cv2.putText(image, '3', (10, 290), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
    cv2.putText(image, '4', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)


def detect_zone(x_center, y_center):
    zone = ''
    if x_center > 320 and y_center < 240:
        zone = 'zone 1'
    elif x_center > 320 and y_center > 240:
        zone = 'zone 2'
    elif x_center <= 320 and y_center >= 240:
        zone = 'zone 3'
    elif x_center <= 320 and y_center <= 240:
        zone = 'zone 4'
    return zone


cap = cv2.VideoCapture(0)

key_stop = 32
key = 0

H_up, H_down, S_up, S_down, V_up, V_down = get_values_from_file('HSV_blue.txt')

HSV_up = [H_up, S_up, V_up]
HSV_down = [H_down, S_down, V_down]

np_HSV_up = numpy.array(HSV_up)
np_HSV_down = numpy.array(HSV_down)

while key != key_stop:
    isRead, image = cap.read()
    image_HSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV_FULL)
    mask = cv2.inRange(image_HSV, np_HSV_down, np_HSV_up)
    cv2.imshow('window_mask', mask)
    contours, service = cv2.findContours(mask,
                                         cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    draw_zones(image)
    for c in contours:
        if len(c) > 40:
            cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
            x_center, y_center = find_center(image, c)
            zone = detect_zone(x_center, y_center)
            cv2.putText(image, zone, (x_center, y_center), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 2)
    cv2.imshow('window', image)
    key = cv2.waitKey(30)
cap.release()
