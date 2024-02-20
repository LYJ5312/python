import cv2
import numpy as np

src=cv2.imread('./data/chessBoard.jpg')
gray=cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

blobF=cv2.SimpleBlobDetector_create()
kp=blobF.detect(gray)
print('len(kp)=',len(kp))
dst=cv2.drawKeypoints(gray, kp, None, color=(0,0,255))

for f in kp: #원 그리기
    r=int(f.size/2)
    cx, cy=f.pt
    cv2.circle(dst,(round(cx),round(cy)),r,(0,0,255),2)

cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()