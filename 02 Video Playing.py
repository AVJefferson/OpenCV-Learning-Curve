import cv2 as cv

capture = cv.VideoCapture("Resources/Videos/dog.mp4")

isTrue = True
while isTrue:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)

# This will cause a no file found error at the end of the video file