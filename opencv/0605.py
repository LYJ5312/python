import cv2
import numpy as np



src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
blur = cv2.GaussianBlur(src, ksize=(7, 7), sigmaX=0.0)
cv2.imshow('src', src)
cv2.imshow('blur', blur)

lap = cv2.Laplacian(src, cv2.CV_32F)#블러처리를 해야 잘땀(사람얼굴 O, 직선처럼 명확한것들은 X)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(lap)
print('lap:', minVal, maxVal, minLoc, maxLoc)
dst = cv2.convertScaleAbs(lap)
dst = cv2.normalize(dst, None, 0, 255, cv2.NORM_MINMAX)
cv2.imshow('lap', lap)
cv2.imshow('dst', dst)

lap2 = cv2.Laplacian(blur, cv2.CV_32F)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(lap2)
print('lap2:', minVal, maxVal, minLoc, maxLoc)
dst2 = cv2.convertScaleAbs(lap2)
dst2 = cv2.normalize(dst2, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('lap2', lap2)
cv2.imshow('dst2', dst2)

cv2.waitKey()
cv2.destroyAllWindows()
