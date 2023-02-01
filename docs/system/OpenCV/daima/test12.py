# 实现鼠标绘制图片
# shape:0 输入l 画直线
# shape:1 输入r 画矩形
# shape:2 输入c 画圆形
import cv2
import numpy as np

shape = 0
start = (0, 0)


cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)


img = np.zeros((360, 640, 3), np.uint8)


def mouse_callback(event, x, y, flags, userdata):
    global shape, start
    print(x, y)
    if (event & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN):
        start = (x, y)
    elif (event & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP):
        if shape == 0:
            cv2.line(img, start, (x, y), (0, 0, 255))
        elif shape == 1:
            cv2.rectangle(img, start, (x, y), (0, 0, 255))
        elif shape == 2:
            a = (x - start[0])
            b = (y - start[1])
            r = int((a**2 + b**2) ** 0.5)
            cv2.circle(img, start, r, (0, 0, 255))
        else:
            print('error')


cv2.setMouseCallback('mouse', mouse_callback, "123")
while True:
    cv2.imshow('mouse', img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        shape = 2
    elif key == ord('r'):
        shape = 1
    elif key == ord('l'):
        shape = 0
cv2.destroyAllWindows()
