import cv2

dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_4X4_50)
marker_image = cv2.aruco.drawMarker(dictionary, 16, 700)
cv2.imshow('window', marker_image)
cv2.waitKey()
cv2.imwrite('marker.png', marker_image)