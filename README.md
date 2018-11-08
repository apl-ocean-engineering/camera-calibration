# camera-calibration
This project will execute a simple intrinsic calibration using OpenCV. A provided script will also capture stills from a video for calibration

## Perequistes and Installing
[Numpy](https://docs.scipy.org/doc/numpy-1.15.1/user/install.html), [OpenCv (for Python2.7)] ((https://docs.opencv.org/3.4.1/d2/de6/tutorial_py_setup_in_ubuntu.html), and glob (sudo pip install glob2) on a Linux machine.  
  
To install, clone repository into desired location

## Codebase

### 'src/image_save.py' 
This file will look for a video file named 'videoIn' (in any cv2 appropriate videofile such as .mp4 or .avi) in the src folder and will begin playing the video. If no video exists (as is initally the case), an exception will be raised.  
With the video screen selected, click 'enter' on the keyboard to save images to the folder  src/calibration_images as .png images.

### src/opencv_calibration.py
This file will loop through all .png photos in src/calibration_images and calibrate the camera using the checkerboard intrinsic calibration technique. As such, all photos in src/calibration_images should be from the same camera and contain a minimum of 8 unique viewpoints for calibration.  
-The src/calibration_images file is initially populated with example images that can be deleted.  
-Images can be manually be placed in src/calibration_images, or placed using image_save.py

## Tutorials
Code based on OpenCv intrisic calibration examples: <https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html>, <https://docs.opencv.org/2.4/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html>



