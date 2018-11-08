#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 08:44:54 2018

Image calibration of SERDP using saved images.

Uses OpenCV Python example code: https://docs.opencv.org/3.4.3/dc/dbb/tutorial_py_calibration.html


@author: mitchell
"""

import numpy as np
import cv2
import glob

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*8,3), np.float32)
objp[:,:2] = np.mgrid[0:8,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob('calibration_images/*.png')

for fname in images:
    img = cv2.imread(fname) #Next image 
    #Convert to grayscale for corner detection
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (8,6),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (8,6), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(500)

"""
calibratecamera(objpoints, imgpoints, imgShape)
Inputs
    objpoints: identical list of vectors specificying 3D point location
    imgpoints: 2D checkerboard points from corner detection
    imgShape: Image size
Outputs
    ret: rms error
    mtx: 3X3 camera matrix
    dist: Distortion coefficients [k1, k2, p1, p2, k3]
    rvecs: Output of rotation vectors for each checkerboard view
    tvecs: Output of translational vectors for each checkerboard view
    
"""
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, 
                                    imgpoints, gray.shape[::-1], None, None)
print(rvecs)
cv2.destroyAllWindows()
