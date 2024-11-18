import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255]
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsvimage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvimage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)

    bbox = mask_.getbox()

    print(bbox)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()

cv2.destroyAllWindows()

