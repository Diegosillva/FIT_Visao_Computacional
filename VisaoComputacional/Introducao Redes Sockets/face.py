import cv2 as cv


webcam = cv.VideoCapture(0, cv.CAP_DSHOW)
rosto = cv.CascadeClassifier("face.xml")
def image():
    global webcam, rosto

    video = webcam.read()[1]

    img_cinza = cv.cvtColor(video, cv.COLOR_BGR2GRAY)

    rostos = rosto.detectMultiScale(img_cinza)
    msg = str(rostos)
    cv.imshow("webcam", video)
    cv.waitKey(1)
    return msg
  




