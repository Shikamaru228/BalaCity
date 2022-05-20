import cv2

image = cv2.imread('WRO2018.png')
height, width, service = image.shape
print(height, width)
for i in range(0, height, 76):
    image[i, 0:width] = [0, 225, 225]
for i in range(0, width, 60):
    image[0:height, i] = [0, 225, 225]
cv2.imshow('window', image)
crop = image[456:533, 720:781]
cv2.imshow('window_crop', crop)
crop_height, crop_width, crop_service = crop.shape
crop_resize = cv2.resize(crop, (crop_width*5, crop_height*5))
cv2.imshow('window_crop_resize', crop_resize)
cv2.waitKey()
cv2.imwrite('face.png', crop_resize)