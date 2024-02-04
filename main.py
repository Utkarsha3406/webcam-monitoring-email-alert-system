import cv2
import time

video = cv2.VideoCapture(0)
time.sleep(1)
while True:

    check,frame = video.read()
    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()

