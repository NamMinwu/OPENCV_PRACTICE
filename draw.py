import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)

# #1. paint the image acertain color
# blank[100:400, 200:300] = 0,0,255
# cv.imshow('Red', blank)
# #2. Draw a Rectangle
# cv.rectangle(blank, (0,0), (250,250),(0,255,0),thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)
# cv.waitKey(0)

#3. Draw A circle
# cv.circle(blank, (250,250) ,40, (0,0,255),thickness=2)
# cv.imshow('Circle', blank)
# cv.waitKey(0)

#4. Draw a line
cv.line(blank, (0,0),(250,250) , (0,0,255),thickness=2)
cv.imshow('line', blank)
#5.Write text
cv.putText(blank, 'Hello',(blank.shape[1]//2, blank.shape[0]//2), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)
cv.waitKey(0)
