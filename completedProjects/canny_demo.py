import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 50, 100)
    cv2.imshow('Canny', canny)


    if cv2.waitKey(1) == 13:
        break

cv2.destroyAllWindows()
