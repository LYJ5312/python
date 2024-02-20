import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 프로그램 시작
# cap = cv2.VideoCapture(0)

cap = cv2.VideoCapture('./data/vtest.avi')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 출력
fig = plt.figure(figsize=(10, 6))  # fig.set_size_inches(10, 6)
fig.canvas.manager.set_window_title('Video capture')
plt.axis('off')

# 입력 처리
def init():
    global im
    retval, frame = cap.read()  # 첫 프레임 캡처
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    # return im,

# 입력 처리
def updateFrame(k):
    retval, frame = cap.read()
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

# function 부분에서 뿌리고 matplot으로 송출
ani = animation.FuncAnimation(fig, updateFrame, init_func=init, interval=50)
plt.show()

if cap.isOpened():
    cap.release()
