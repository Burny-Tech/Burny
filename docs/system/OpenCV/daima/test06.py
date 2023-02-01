# 设置鼠标回调函数

# setMouseCallback( winname, callback, userdata)
# callback (event , x ,y ,flags, userdata)
# event :鼠标移动，按下左键右键等，
# flags:键盘ctrl shift alt + 组合键

import cv2
import numpy as np


def mouse_call_back(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)


cv2.namedWindow('mouse', cv2.WINDOW_NORMAL)

cv2.resizeWindow('mouse', 640, 360)

cv2.setMouseCallback('mouse', mouse_call_back, '123')

img = np.zeros((360, 640, 3), np.uint8)

while True:
    cv2.imshow('mouse', img)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
