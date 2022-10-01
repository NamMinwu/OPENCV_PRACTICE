import cv2 as cv

def rescaleFrame(frame, scale=.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# img resizing
# img = cv.imread('Photos/cat.jpg')
# resize_img = rescaleFrame(img)

# cv.imshow('Cat1',img)
# cv.imshow('Cat2', resize_img)

# cv.waitKey(0)

#  Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video_resize', frame_resized)
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()   


# on my camera
def chageRes(width, height):
    #Live video
    capture.set(3,width)
    capture.set(4,height)
capture = cv.VideoCapture('Videos/dog.mp4')


