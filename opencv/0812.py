import cv2
import numpy as np

src = cv2.imread('./data/banana.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
ret, bImage = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

bImage = cv2.dilate(bImage, None)
cv2.imshow('src',src)
cv2.imshow('gray',gray)
cv2.imshow('bImage',bImage)

# Find contours in the binary image
contours, _ = cv2.findContours(bImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

maxLength = 0
k = 0
for i, cnt in enumerate(contours):
    perimeter = cv2.arcLength(cnt, closed=True)
    if perimeter > maxLength:
        maxLength = perimeter
        k = i

print('maxLength=',maxLength)
cnt = contours[k]
dst2 = src.copy()
cv2.drawContours(dst2,[cnt],0,(255, 0, 0), 3)

area = cv2.contourArea(cnt)
print('area=',area)
x, y, width, height = cv2.boundingRect(cnt)
dst3 = dst2.copy()
cv2.rectangle(dst3, (x, y), (x+width, y + height), (0,0,255),2)
cv2.imshow('dst3',dst3)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int32(box)
print('box=',box)
dst4 = dst2.copy()
cv2.drawContours(dst4,[box],0,(0,0,255),2)
cv2.imshow('dst4',dst4)

(x, y),radius = cv2.minEnclosingCircle(cnt)
dst5 = dst2.copy()
cv2.circle(dst5,(int(x), int(y)), int(radius), (0,0,255),2)
cv2.imshow('dst5',dst5)

cv2.waitKey()
cv2.destroyAllWindows()
