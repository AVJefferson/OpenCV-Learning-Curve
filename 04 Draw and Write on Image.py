import cv2 as cv
import numpy as np

#img = cv.imread("Resources/Images/cat.jpg")
blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('blank', blank)
cv.waitKey(250)


# RGB Filling Color
blank[:] = 0,255,0
cv.imshow('blank', blank)
cv.waitKey(250)

#RGB Filling Partially
blank[200:300, 200:300] = 255,0,100
cv.imshow('blank', blank)
cv.waitKey(250)


#Drawing a rectange
cv.rectangle(blank, (100,100), (400,400), (0,0,255), 10)
cv.imshow('blank', blank)
cv.waitKey(250)

#Drawing a filled rectange (cv.FILLED = -1)
cv.rectangle(blank, (0,0), (100,500), (125,125,125), cv.FILLED)
cv.imshow('blank', blank)
cv.waitKey(250)

#Drawing a filled rectange (cv.FILLED = -1)
cv.rectangle(blank, (blank.shape[1]//2, blank.shape[0]//2), (blank.shape[1], blank.shape[0]), (125,125,125), cv.FILLED)
cv.imshow('blank', blank)
cv.waitKey(250)


#Drawing Circle
cv.circle(blank, (30,30), 25, (0,0,255), 3)
cv.imshow('blank', blank)
cv.waitKey(250)

#Drawing Circle
cv.circle(blank, (30,30), 25, (0,0,255), -1)
cv.imshow('blank', blank)
cv.waitKey(250)


#Drawing Line
cv.line(blank, (30,30), (400,400), (255,255,255), 3)
cv.imshow('blank', blank)
cv.waitKey(250)

#Writing Text
cv.putText(blank, "Hello World", (25,25), cv.FONT_HERSHEY_TRIPLEX, 1.0, (25, 25, 25), 2)
cv.imshow('blank', blank)
cv.waitKey(250)