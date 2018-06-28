import numpy as np
import cv2

def myfunc(i):
    pass # do nothing

cv2.namedWindow('title') # create win with win name

cv2.createTrackbar('gaussian', 'title', 0, 10, myfunc)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()

    g = cv2.getTrackbarPos('gaussian','title')
    blur = cv2.GaussianBlur(frame, (g, g), 5)
    cv2.imshow('title', blur)  # show in the win
    key = cv2.waitKey(10)
    if key == 27:  # ESCキーで終了
        break

cap.release()
cv2.destroyAllWindows()
