from PPTControler import PPTControler
from GestureRecognition import Recognizer
import cv2

if __name__ == '__main__':
    R = Recognizer()
    while(1):
        R.detect()
        if cv2.waitKey(1) & 0xFF == 27:
            break