#커널은 먼저 x축 y축에 대해서 만들어야함
#축은 getDerivKernels 숫자를 변경해서 각 x, y축을 설정하고 합해서 영역 설정 이후 농도차이를 만듬

import cv2
import numpy as np

src =  cv2.imread('./data/alphabet.bmp', cv2.IMREAD_GRAYSCALE)

kx, ky = cv2.getDerivKernels(1, 0, ksize=3)
sobelX = ky.dot(kx.T)

print('kx=',kx)
print('ky=',ky)
print('sobelX=',sobelX)
gx = cv2.filter2D(src, cv2.CV_32F, sobelX)

kx, ky = cv2.getDerivKernels(0, 1, ksize=3)
sobelY =ky.dot(kx.T)

print('kx=', kx)
print('ky=', ky)
print('sobelY=', sobelY)
gy = cv2.filter2D(src, cv2.CV_32F, sobelY)

mag = cv2.magnitude(gx, gy)#두 축의 그라디언트를 사용하여 magnitude 계산
ret, edge = cv2.threshold(mag, 100, 255, cv2.THRESH_BINARY)

cv2.imshow('edge',edge)
cv2.waitKey()
cv2.destroyAllWindows()