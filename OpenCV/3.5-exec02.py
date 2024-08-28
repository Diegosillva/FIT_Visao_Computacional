import cv2 as cv
import numpy as np

img = cv.imread("imagens/biometria.jpg")

kernel = np.ones((5, 5))
# resultado = cv.dilate(img, kernel)
# resultado = cv.medianBlur(img, 7)
resultado = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
cv.imshow("Original", img)
cv.imshow("Modificada", resultado)
cv.waitKey(0)
cv.destroyAllWindows()
