import cv2

cap=cv2.VideoCapture('./data/vtest.avi')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

format_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
               int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size=',format_size)

#fourcc = cv2.VideoWriter_fourcc(*'DIVX') #('D','I','V','X')
fourcc = cv2.VideoWriter_fourcc(*'XVID')

out1 = cv2.VideoWriter('./data/record0.mp4',fourcc,20.0, format_size)
out2 = cv2.VideoWriter('./data/record1.mp4',fourcc,20.0, format_size,isColor=False)

while True:
    retval, frame = cap.read()
    if not retval:
        break
    out1.write(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(gray)
    cv2.imshow('frame', frame)
    cv2.imshow('gray',gray)

    key = cv2.waitKey(25)
    if key==27:
        break
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()