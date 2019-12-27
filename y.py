import argparse
import dlib
from scipy.spatial import distance as dist
from imutils.video import VideoStream
import cv2
ap = argparse.ArgumentParser()
import imutils
ap.add_argument("-w", "--webcam", type=int, default=0,help="index of webcam on system")
args = vars(ap.parse_args())
vs = VideoStream(src=args["webcam"]).start()
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_5_face_landmarks.dat")
frame = vs.read()
#frame=cv2.imread("fr.jpg")
frame = imutils.resize(frame)
cv2.imwrite("fr.jpg",frame)
print(frame)
while 1==1:
    cv2.imshow('frame', frame)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# detect faces in the grayscale frame
print("x")
rects = detector(gray, 0)
print(rects)
