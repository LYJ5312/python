import cv2
import matplotlib.pyplot as plt

def handle_key_press(event):
    if event.key == 'escape':
        cap.release()
        plt.close()

def handle_close(evt):
    print('Figure closed')
    cap.release()

# Program start
cap = cv2.VideoCapture(0)  # Camera index 0

plt.ion()  # Interactive mode
fig = plt.figure(figsize=(10, 6))
plt.axis('off')
fig.canvas.manager.set_window_title('Video Capture')
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_event', handle_close)

retval, frame = cap.read()
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

while True:
    retval, frame = cap.read()  # Capture frame
    if not retval:
        break
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    fig.canvas.draw()
    fig.canvas.flush_events()

if cap.isOpened():
    cap.release()
 #들어오는 데이터가 달라질때마다 출력하는 형식