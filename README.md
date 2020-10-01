# Facial_Landmark_detection
Small application using dlib and OpenCV to extract facial landmarks from a person's face

#### How to install:
Requires pip to run.

```sh
$ pip install opencv-pyt
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libgtk-3-dev
$ sudo apt-get install libboost-all-dev
$ pip install scipy
$ pip install scikit-image
$ pip install dlib
$ pip install imutils
```

  
 #### How to run:
- python3 'file'.py

#### Examples description:
- webcam_test.py is a small test to see if your webcam its working correctly. Once you run the code you should be able to see a new window if your webcam image
- landmark_image.py is an experiment running landmark detection over a few image samples which are into the 'images' foldes. All files are .jpg images
- landmark_realTime.py is another experiment running real time landmark detection over your webcam image
