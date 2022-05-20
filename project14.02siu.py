import cv2
import numpy

def read_values_from_file(filename):
    file = open(filename, 'r')
    values = file.read()
    values_split = values.split(',')
    for number in range(6):
        values_split[number] = int(values_split[number])
    file.close()
    return values_split

def find_minAreaRect(contour, image):
    rect = cv2.minAreaRect(contour)
    x_center, y_center = rect[0]
    cv2.circle(image, (int(x_center), int(y_center)), 15, (255, 0, 255), -1)
    points = cv2.boxPoints(rect)
    points_int = numpy.array(points, int)
    cv2.drawContours(image, [points_int], 0, (255, 0, 0), 15)
    print(points)
