import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hue = hsv_frame[75,320,0]
    print hue
    if hue < 50:
        print 'yellow'
        cv2.putText(frame, 'Yellow!', (200, 300), cv2.FONT_HERSHEY_COMPLEX, 2, (0,125,125), 1)
    if hue < 105 and hue > 95:
        print 'blue'
        cv2.putText(frame, 'Blue!', (200, 300), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 1)
    if hue < 169 and hue > 150:
        print 'pink'
        cv2.putText(frame, 'Pink!', (200, 300), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255), 1)

    cv2.circle(frame, (320, 75), 15, (155,155,255), -1)
    cv2.imshow('Webcam feed', frame)
#
#
#
    if cv2.waitKey(1) == 13:
        break
#
#
#
cap.release()
cv2.destroyAllWindows()

# print 'helo'
