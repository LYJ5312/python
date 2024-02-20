import cv2
src = cv2.imread('./data/lena.jpg')

b,r,g = cv2.split(src)

cv2.imshow('blue', b)
cv2.imshow('green', r)
cv2.imshow('red', g)

dst = cv2.merge([b, r, g])

cv2.imshow('dst',dst)

cv2.waitKey()
cv2.destroyAllWindows()