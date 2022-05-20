import cv2

image = cv2.imread('cow.jpeg')
image[440:600, 400:610] = [225, 0, 0]
cv2.imshow('window', image)
crop = image[150:250, 650:800]
cv2.imshow('window_crop', crop)
print(image.shape)
cv2.waitKey()