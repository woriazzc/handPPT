from PPTControler import PPTControler
from GestureRecognition import Recognizer


if __name__ == '__main__':
    R = Recognizer()
    while(1):
        R.detect()