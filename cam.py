import cv2
import sys
from recognize import *

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
#cam = cv2.VideoCapture(0)


def run(gray, dh, dw):
    stop = False
    rval = True
    #if cam.isOpened(): # try to get the first frame
    #    rval, frame = cam.read()
    #else:
    #    rval = False
    #    print "Camera is not found"
    #while rval or not stop:
        #ret, frame = cam.read()
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#print('working')
        #cv2.imshow('frame',frame)
	#if cv2.waitKey(1) & 0xFF == ord('q'):
        #	break
    faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30, 30),
	flags=cv2.cv.CV_HAAR_SCALE_IMAGE
     )
	
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
	#cv2.rectangle(gray, (x, y), (x+w, y+h), (0, 255, 0), 2)
	center = (x+w/2,y+h/2)
	#cv2.circle(gray,center, 10, (0,0,255), -1)
	#cv2.imshow('frame',frame)
	return True, center
    return False, (10,10)
    #return (map(lambda (gray.shape)
    #cam.release()
    #cv2.destroyAllWindows()
