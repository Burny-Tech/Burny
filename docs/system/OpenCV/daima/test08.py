# 色彩空间
# 像素访问
# 矩阵的 + - *  /
# 基本图形的绘制

# RGB: 人眼的色彩空间
# OpenCV 默认使用BGR
# HSV/HSB/HSL
# HSV: 色相 饱和度 明亮度
# YUV:

# HSV
# Hue: 色相,即色彩，如红色，蓝色，
# Saturation : 饱和度，颜色的纯度
# Value: 明度
# ('./public/images/HSV001.png')
# ('./public/images/HSV002.png')
# ('./public/images/HSV003.png')


# HSL
# 亮度不同
# HUE SATURATION LIGHT
# ('./public/images/HSL HSV 的区别.png')

# YUV: 色彩空间转换，主要用于视频中。

# YUV4:2:0
# YUV4:2:2
# YUV4:4:4
# 4个Y 2个U 0 个V
# 黑白只有Y 。彩色兼容黑白电视产生YUV


# 色彩空间转换

import cv2

cv2.namedWindow('color', cv2.WINDOW_NORMAL)
img = cv2.imread('./public/images/HSV001.png')


def callback(values):
    print(values)


colorspaces = [cv2.COLOR_BGR2RGB, cv2.COLOR_BGR2RGBA,
               cv2.COLOR_RGB2GRAY, cv2.COLOR_BGR2HSV_FULL]

img = cv2.imread('./public/images/HSV001.png')

cv2.createTrackbar('curcolor', 'color', 0, len(colorspaces), callback)


while True:
    index = cv2.getTrackbarPos('curcolor', 'color')

# 颜色空间转换API
    cvt_img = cv2.cvtColor(img, colorspaces[index-1])
    cv2.imshow('color', cvt_img)
    key = cv2.waitKey(10)
    if key & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
