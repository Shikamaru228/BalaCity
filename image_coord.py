import cv2

image = cv2.imread('flower.jpeg')
print(image.shape)
print(image[599,1149])
print(image[0,0])
cv2.imshow('window',image)
cv2.waitKey()