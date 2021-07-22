from PPTControler import PPTControler
from GestureRecognition import Recognizer
import cv2

if __name__ == '__main__':
    R = Recognizer()
    stat = 0
    while True:
        gesture_str = R.detect()
        if gesture_str:
            if gesture_str == "fist":
                stat = 1
            elif gesture_str == 'love':
                stat = 2
            elif gesture_str == 'two':
                stat = 3
            elif gesture_str == 'thumbUp' and stat == 1:
                stat = 4
            else:
                stat = 0
            if stat == 2:
                PPTControler().fullScreenWithCurPage()
            elif stat == 3:
                PPTControler().endPlay()
            elif stat == 4:
                PPTControler().click()
            if stat != 1:
                stat = 0
        if cv2.waitKey(1) & 0xFF == 27:
            break
