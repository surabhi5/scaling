# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 11:08:17 2018

@author: SURABHI
"""

import cv2
print(cv2.__version__)
cap = cv2.VideoCapture(0)    
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)

while True:
    ret,frame=cap.read()
  
    frame=rescale_frame(frame,percent=90)
    frame1=rescale_frame(frame,percent=50)
    frame2=rescale_frame(frame,percent=140)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
    cv2.imshow('gray',gray)
    cv2.imshow('frame2',frame)
    cv2.imshow('hsv',hsv)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    