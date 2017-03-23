import cv2
import numpy as np

image = cv2.imread('images/house.jpg')

original_image = image.copy()
cv2.imshow('Original image', original_image)
cv2.waitKey()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print 'contours length:', len(contours)

# for c in contours:
#     x,y,w,h = cv2.boundingRect(c)
#     cv2.rectangle(original_image, (x,y), (x+w, y+h), (0, 0, 255),2)
#     cv2.imshow('Bounding Rectangle', original_image)
#     cv2.waitKey()

for c in contours:
    accuracy = 0.0000001 * cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c, accuracy, True)
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    cv2.imshow('Approx poly DP', image)
    cv2.waitKey()

cv2.waitKey()
cv2.destroyAllWindows()
