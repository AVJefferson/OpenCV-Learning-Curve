import cv2 as cv
capture = cv.VideoCapture(0)


# Works with Images, Videos, Live Videos
def rescaleframe (frame, scale = 0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
     
    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)



#Only works with Live Video - Camera feed
def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)
    return



while True:
    isTrue, frame = capture.read()
    frame_new = rescaleframe(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video New', frame_new)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()
cv.destroyAllWindows()

cv.waitKey(0) 