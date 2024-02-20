import cv2
import numpy as np 

src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
dst = np.zeros(src.shape, dtype=src.dtype)

N = 64  # 8, 32, 64
height, width = src.shape

h = height // N
w = width // N
for i in range(N):
    for j in range(N):
        y = i * h  # Use i for row index
        x = j * w  # Use j for column index
        roi = src[y:y+h, x:x+w]
        dst[y:y+h, x:x+w] = cv2.mean(roi)[0]
        # dst[y:y+h, x:x+w] = cv2.mean(roi)[0:3]  # Commented out to avoid an error

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
