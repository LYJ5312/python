import numpy as np
import cv2

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0

while True:
    key = cv2.waitKeyEx(30)
    if key == 27:  # ESC 키
        break

    elif key == 0x270000:
        direction = 0
    elif key == 0x280000:
        direction = 1
    elif key == 0x250000:
        direction = 2
    elif key == 0x260000:
        direction = 3

    if direction == 0:
        x += 10
    elif direction == 1:
        y += 10
    elif direction == 2:
        x -= 10
    else:
        y -= 10

    if x < R:
        x = R
        direction = 0
    if x > width - R:
        x = width - R
        direction = 2
    if y < R:
        y = R
        direction = 1
    if y > height - R:
        y = height - R
        direction = 3  # 수정: direction 변수 할당 누락

    img = np.zeros((width, height, 3), np.uint8) + 255
    # 수정: cv2.circle 호출 부분에서 쉼표(,)로 구분되어야 함
    cv2.circle(img, (x, y), R, (0, 0, 255), -1)
    cv2.imshow('img', img)

cv2.destroyAllWindows()
