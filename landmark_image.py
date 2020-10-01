#Small application using real-time landmark detections 

#Import the libs which we need
from imutils import face_utils, resize
import dlib
import cv2
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import numpy as np
import os
# @brief:   This Function will get the path+name of files csv
# @param:   path is the path where the csv files are
# @return:  return a list of str path+filename
def findFiles(path,typeFile):
    paths = [os.path.join(path, name) for name in os.listdir(path)]
    files = [arq for arq in paths if os.path.isfile(arq)]
    csvs = [arq for arq in files if arq.lower().endswith(typeFile)]
    csvs.sort()
    #print("From path: Files founded: %d"%(len(csvs)))
    return csvs
#END


# let's go code an faces detector(HOG) and after detect the 
# landmarks on this detected face
# p = our pre-treined model directory, on my case, it's on the same script's diretory.
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

#Find all images into the folder
imgs = findFiles('images','jpg')
 

for x in imgs:
    print("Sample: ", x)
    # load the input image, resize it, and convert it to grayscale
    path = 'images/'
    image = cv2.imread(x)
    image = resize(image, width=500)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
    # Get faces into webcam's image
    rects = detector(gray, 0)
    
    # For each detected face, find the landmark.
    for (i, rect) in enumerate(rects):
        # Make the prediction and transfom it to numpy array
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
    
        # Draw on our image, all the finded cordinate points (x,y) 
        for (x, y) in shape:
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)
    
    # Show the image
    cv2.imshow("Output", image)
    #Press any key (with the image opened) to continue
    cv2.waitKey()
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()