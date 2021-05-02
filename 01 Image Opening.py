import cv2 as cv

img1 = cv.imread("Resources/Images/cat.jpg")
img2 = cv.imread("Resources/Images/cat_large.jpg")

cv.imshow('Cat', img1)
cv.imshow('Cat_Large', img2)

cv.waitKey(0)
