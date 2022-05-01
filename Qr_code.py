import time

import cv2
import numpy as np
from pyzbar.pyzbar import decode


def scanner():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    mydata = 1

    while True:
        success, img = cap.read()
        for qrcode in decode((img)):
            mydata = list(qrcode.data.decode('utf-8').split())
            # print(mydata)
            pts= np.array([qrcode.polygon], np.int32)
            pts = pts.reshape(-1, 1, 2)
            cv2.polylines(img, [pts], True, (0, 255, 0), 5)
            pts2 = qrcode.rect
            cv2.putText(img, mydata[0], (pts2[0], pts2[1]), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0,255,0),2)

        cv2.imshow('Result', img)
        cv2.waitKey(1)
        if(mydata != 1):
            cv2.waitKey(3)
            break

    return mydata
