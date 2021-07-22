from PPTControler import PPTControler
from GestureRecognition import Recognizer
import cv2

clk = 0
if __name__ == '__main__':
    R = Recognizer()
    stat = 0
    while True:
        if clk % 20 == 0:
            gesture_str = R.detect()
            if gesture_str:
                if gesture_str == "fist":
                    stat = 1
                elif gesture_str == 'thumbUp' and stat == 1:
                    stat = 2
                elif gesture_str == 'five' and stat == 1:
                    stat = 3
                else:
                    stat = 0
                if stat == 2:
                    PPTControler().fullScreen()
                elif stat == 3:
                    PPTControler().click()
                if stat != 1:
                    stat = 0
        if cv2.waitKey(1) & 0xFF == 27:
            break
        clk += 1
