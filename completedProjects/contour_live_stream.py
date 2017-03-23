import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    grayCopy = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(grayCopy, 50, 100)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print "# of Contours:", str(len(contours))
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows
