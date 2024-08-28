import cv2 as cv

pessoas = cv.imread("imagens\pessoas.jpg")

gray = cv.cvtColor(pessoas, cv.COLOR_BGR2GRAY)

classificador_rosto = cv.CascadeClassifier("face.xml")
rosto = classificador_rosto.detectMultiScale(gray)


for x, y, w, h in rosto:
    cv.rectangle(pessoas, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv.imshow("Pessoas", pessoas)
cv.waitKey(0)
