import cv2
from PIL import Image
import numpy as np


#function

def get_limits(color):
    c = np.uint8([[color]])

    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 10, 100, 100
    upperLimit = hsvC[0][0][0] + 10, 255, 255 

    lowerLimit = np.array(lowerLimit, dtype = np.uint8)
    upperLimit = np.array(upperLimit, dtype = np.uint8)

    return lowerLimit, upperLimit

red = [255, 0, 0]
lower_color = np.array([170, 50, 50])
upper_color = np.array([180, 255, 255])
video = cv2.VideoCapture('object_video.mp4')

if (video.isOpened == False):
    print("Error opening video file")

while True:
    ret, frame = video.read()

    widht = 900
    height = 540
    dim = (widht, height)

    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

    hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #lowerLimit, upperLimit = get_limits(red)
    mask = cv2.inRange(hsvimage, lower_color, upper_color)

    masked = Image.fromarray(mask)

    bbox = masked.getbbox()

    if bbox is not None:
        print("1")
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    else:
        print("0")

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


video.release()

cv2.destroyAllWindows()


