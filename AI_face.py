#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: kang_liu
import cv2
import os
import numpy as np
from Access_Token import Mactch
import time

Camera = cv2.VideoCapture(0)

while(True):
    ret, frame = Camera.read()
    face_cascade = cv2.CascadeClassifier('./FaceRecognition/haarcascade_frontalface_default.xml') 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x, y, w, h) in faces:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)  
    cv2.imshow('faceMe',frame)

    if cv2.waitKey(1) & 0xFF == 27:  
        cv2.imwrite('faceMe.jpg',frame)
        break 
Camera.release()
cv2.destroyAllWindows()


time_start = time.time()
try:
    for files in os.walk('FaceFile'):
        data = files[-1] 
    for i in data:
        tag = 'FaceFile/' + i 
        result = Mactch('faceMe.jpg',tag)

    print('result:{}'.format(result))
    time_end = time.time()
    print('timeCost:{} s'.format(time_end-time_start))
    score = result[-1][1]
    if score <= 50:
        text = 'Name:Stranger'
        img = cv2.imread('faceMe.jpg')
        cv2.putText(img, text, (10, 35), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('FaceMe', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        text = 'Name:{}'.format(result[-1][0])
        img = cv2.imread('faceMe.jpg')
        cv2.putText(img,text, (10, 40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0),2) 
        cv2.imshow('FaceMe',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
except:
    print('internet error')

