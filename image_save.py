#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 16:16:51 2018

@author: mitchell
@contact: miscott@uw.edu


Python OpenCV script to save SERDP camera images
"""
import numpy as np
import cv2 as cv


#Load camera calibration video
cap = cv.VideoCapture('haptic1-20181107-130300.mp4') #calibration video file
im = 0 #Tracker to count image frames
while(True):
    #Read the frame and display
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    #Check if enter key is pressed, if so, exit
    key = cv.waitKey(1) 
    if key == 10: #10 indicates the 'enter' key was pressed
        name = 'calibration_images/frame%s.png' % (im)
        cv.imwrite(name, frame) 
    # cntrl+c to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    im += 1
    
#Destroy the windows
cap.release()
cv.destroyAllWindows()