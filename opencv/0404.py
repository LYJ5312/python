import cv2

img = cv2.imread('./data/lena.jpg')
img[100,200] = [255,0,0]
print(img[100, 200:210])

##for y in range(100, 400):
#     for x in range(200, 300)
#         img[y ,x]=0

img[100:400, 200:300]=[255,0,0]

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()