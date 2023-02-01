# trackBar 控件

# createTrackbar()
# 参数：trackbarname,winname
# 参数: value:trackbar 当前值
# 参数：count: 最小值为0 最大值为count
# 参数：callback ，userdata

# getTrackbarPos()
# 参数：trackbarname:,winname
# 输出： 当前值

import cv2
import numpy as np


def call_back(value):
    print(value)


cv2.namedWindow('trackbar', cv2.WINDOW_NORMAL)
cv2.createTrackbar('R', 'trackbar', 0, 255, call_back)
cv2.createTrackbar('G', 'trackbar', 0, 255, call_back)
cv2.createTrackbar('B', 'trackbar', 0, 255, call_back)

# 纯黑色图片 3 层
img = np.zeros((480, 360, 3), np.uint8)

while True:

    r = cv2.getTrackbarPos('R', 'trackbar')
    g = cv2.getTrackbarPos('G', 'trackbar')
    b = cv2.getTrackbarPos('B', 'trackbar')
    img[:] = [r, g, b]
    cv2.imshow('trackbar', img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
