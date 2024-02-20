import cv2
import numpy as np

def get_RBG_in_image(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        print("마우스가 눌린 위치의 HSV값은:{}".format(param['image'][y,x,:]))

    if event == cv2.EVENT_RBUTTONUP:
        print("마우스오른쪽 버튼이 눌린 위치와 비슷한 색상을 가진 픽셀만 뽑기")
        threshold = 25
        value = param['image'][y,x,:]
        mask = cv2.inRange(param['image'],value - threshold,
                           value + threshold)
    
        range_image = cv2.bitwise_and(param['image'],param['image'],
                                      mask = mask)
        cv2.imshow("range_image", range_image)
    return


origin_image = cv2.imread('./data/mango2.jpg')
hsv = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)
param = {
    'image' : origin_image
}
cv2.imshow('image', origin_image)
cv2.setMouseCallback('image', get_RBG_in_image,param)
cv2.waitKey(0)
cv2.destroyAllWindows()