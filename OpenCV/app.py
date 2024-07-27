import cv2 as cv
img = cv.imread('imagens/fit.png',cv.IMREAD_GRAYSCALE)

cv.imshow('Logo FIT', img)
cv.waitKey(0)