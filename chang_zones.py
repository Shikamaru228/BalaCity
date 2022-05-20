import cv2

image = cv2.imread('cars_stream.jpeg')
image[50, 0:900] = [0, 0, 225]
for i in range(0, 600, 50):
    image[i, 0:900] = [0, 0, 250]
for i in range(0, 900, 50):
    image[0:600, i] = [0, 0, 250]
cv2.imshow('window', image)
print(image.shape)
cv2.waitKey()