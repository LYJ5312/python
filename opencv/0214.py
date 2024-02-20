import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Video(animation.FuncAnimation):
    def __init__(self, device=0, fig=None, frames=None,
                 interval=50, repeat_delay=5, blit=False, **kwargs):
        
        if fig is None:
            self.fig = plt.figure()
            self.fig.canvas.manager.set_window_title('Video Capture')
            plt.axis("off")
        
        # super는 animation(알맹이)를 가리킴
        super(Video, self).__init__(self.fig, self.updateFrame, init_func=self.init,
                                    frames=frames, interval=interval, blit=blit,
                                    repeat_delay=repeat_delay, **kwargs)
        self.cap = cv2.VideoCapture(device)
        print("start capture")

    def init(self):
        retval, self.frame = self.cap.read()
        if retval:
            self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

    def updateFrame(self, k):
        retval, self.frame = self.cap.read()
        if retval:
            self.im.set_array(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))  # 수정: camera.frame을 self.frame으로 변경

    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print("finish capture.")

# 프로그램 시작
# camera = Video()
camera = Video('./data/vtest.avi')

plt.show()
camera.close()
