import cv2
import numpy as np

image = cv2.imread('images/bunchofshapes.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 50, 200)

cv2.imshow('canny', edged)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


cv2.drawContours(image, contours, -1, (0,0,255), 3)

def x_cord_contour(contour):
    M = cv2.moments(contour)
    return int(M['m10'] / M['m00'])

sorted_contours = sorted(contours, key=x_cord_contour, reverse = False)

for (i, c) in enumerate(sorted_contours):

    moment = cv2.moments(c)
    cx = int(moment['m10'] / moment['m00'])
    cy = int(moment['m01'] / moment['m00'])
    (x,y,w,h) = cv2.boundingRect(c)

    cropped_contour = image[y:y+h, x:x+w]

    cv2.imshow('cropped', cropped_contour)
    cv2.imwrite('cropped' + str(i+1) + '.jpg', cropped_contour)
    cv2.waitKey(0)


cv2.destroyAllWindows()
