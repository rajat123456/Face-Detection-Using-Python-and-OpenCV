# Face Detection

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # loading the cascade for the face.
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') # loading the cascade for the eyes.

def detect(gray, frame): # creating a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles. 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # applying the detectMultiScale method from the face cascade to locate one or several faces in the image.
    for (x, y, w, h) in faces: # For each detected face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # painting a rectangle around the face.
        roi_gray = gray[y:y+h, x:x+w] # getting the region of interest in the black and white image.
        roi_color = frame[y:y+h, x:x+w] # getting the region of interest in the colored image.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) # applying the detectMultiScale method to locate one or several eyes in the image.
        for (ex, ey, ew, eh) in eyes: # For each detected eye:
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 2) # painting a rectangle around the eyes, but inside the referential of the face.
    return frame # returning the image with the detector rectangles.

video_capture = cv2.VideoCapture(0) # turning the webcam on.

while True: # repeat infinitely (until break):
    _, frame = video_capture.read() # getting the last frame.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # doing some colour transformations.
    canvas = detect(gray, frame) # getting the output of our detect function.
    cv2.imshow('Video', canvas) # displaying the outputs.
    if cv2.waitKey(1) & 0xFF == ord('q'): # If we type on the keyboard:
        break # stop the loop.

video_capture.release() # turn the webcam off.
cv2.destroyAllWindows() # destroy all the windows inside which the images were displayed.
