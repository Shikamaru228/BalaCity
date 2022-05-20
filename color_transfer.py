import cv2
from paho.mqtt.client import Client

device = Client("project")
device.username_pw_set("dm228", "Ra258456")
device.connect("mqtt.pi40.ru", 1883)



cap = cv2.VideoCapture(1)

key = -1

while key == -1:
    isRead, image = cap.read()
    p = image[120, 480]
    b, g, r = p
    p2 = image[360, 480]
    b2, g2, r2 = p2
    p3 = image[120, 160]
    b3, g3, r3 = p3
    p4 = image[360, 160]
    b4, g4, r4 = p4
    cv2.line(image, (0, 240), (639, 240), (255, 0, 0))
    cv2.line(image, (320, 0), (320, 479), (255, 0, 0))
    cv2.circle(image, (480, 120), 30, (int(b), int(g), int(r)), -1)
    cv2.circle(image, (480, 360), 30, (int(b2), int(g2), int(r2)), -1)
    cv2.circle(image, (160, 120), 30, (int(b3), int(g3), int(r3)), -1)
    cv2.circle(image, (160, 360), 30, (int(b4), int(g4), int(r4)), -1)
    if b > 60 and g < 60 and r < 60:
        cv2.putText(image, 'zone 1', (330, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        device.publish("dm228/zone1", "человек тонет в зоне 1")
    if b2 > 60 and g2 < 60 and r2 < 60:
        cv2.putText(image, 'zone 2', (330, 290), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        device.publish("dm228/zone2", "человек тонет в зоне 2")
    if b3 > 60 and g3 < 60 and r3 < 60:
        cv2.putText(image, 'zone 3', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        device.publish("dm228/zone3", "человек тонет в зоне 3")
    if b4 > 60 and g4 < 60 and r4 < 60:
        cv2.putText(image, 'zone 4', (10, 290), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        device.publish("dm228/zone4", "человек тонет в зоне 4")
    cv2.imshow('window', image)
    key = cv2.waitKey(20)
print(10, 290)
cap.release()