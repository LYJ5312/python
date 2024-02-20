import cv2

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
rects = cv2.selectROIs('src',src,False,True)
print('rects=',rects)

for r in rects:
    cv2.rectangle(src, (r[0], r[1]), (r[0]+r[2], r[1]+r[3]), 255)



cv2.imshow('src',src)
cv2.waitKey()
cv2.destroyAllWindows()