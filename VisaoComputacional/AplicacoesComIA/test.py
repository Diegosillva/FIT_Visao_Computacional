import cv2 as cv

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    cap, frame = webcam.read()
    
    cv.imshow("Capture", frame)
    if cv.waitKey(0) == ord("q"):
        break
