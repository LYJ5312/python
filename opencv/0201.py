import cv2
import numpy as np

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile) #cv.IMREAD_COLOR
img2 = cv2.imread(imageFile, 0) #CV2.IMREAD_GRAYSCALE 0을 줌으로써 그레이스케일

##encode_img = np.fromfile(imageFile,np.unit8)
##img = cv2.imdecode(encode_img, cv2.IMREAD_UNCHANGED)

cv2.imshow('Lena color',img)
cv2.imshow('Lena grayscale',img2)

cv2.waitKey()
cv2.destoryAllWindows()