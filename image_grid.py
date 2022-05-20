import cv2

image =cv2.imread('cars.jpeg')
image[50, 100] = [0, 0, 255]
image[50, 101] = [0, 0, 255]
image[50, 99] = [0, 0, 255]
image[50, 100:300] = [0, 0, 255]
image[50:250, 100] = [0, 0, 225]
image[250, 100:300] = [0, 0, 225]
image[50:250, 300] = [0, 0, 225]
cv2.imshow('window',image)
print(image.shape)
cv2.waitKey()