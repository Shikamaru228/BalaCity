import cv2

image = cv2.imread('1446123907_doroga_asfalt_solnce_svet_bliki_polden_reka_bereg_razmetka_linii_dvoynaya_sploshnaya_kraska_oblaka_obemnye_62343_1920x1080 (1).jpg')
image[30,50:70] = [0, 0, 225]
crop = image[20:50, 50:70]
cv2.imshow('window',image)
cv2.imshow('window2', crop)
cv2.waitKey(7000)
print(image[100,100])
height, width, service = image.shape
image_resize = cv2.resize(image, (width*2, height*2))
cv2.imshow('window200-2', image_resize)
image_resize_small = cv2.resize(image, (int(width*0.5), int(height*0.5)))
cv2.imshow('window50', image_resize_small)
cv2.imwrite('MyPicture.png', image_resize_small)
image1 = cv2.imread('RGB-color-model.png')
print(image1[100,100])
print(image1[200,200])
print(image1[300,400])
print(image1.shape)
for i in range(0, 800, 10):
    image1[i, 0:800] = [0, 225, 0]
for i in range(0, 800, 10):
    image1[0:800, i] = [0, 225, 0]
cv2.imshow('window3', image1)
cv2.waitKey()