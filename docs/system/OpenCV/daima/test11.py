# OpenCV 绘制图形
'''
line(img,开始点，结束点，颜色,线宽，线型)

ellipse(img,中心点，（长的一半，宽的一半），倾斜角度，从哪个角度开始，到哪个角度结束，颜色，线宽，线性)
polylines(img,点集(32位的)，是否闭环，颜色，...)

画文本
putText(img,字符串，起始点，字体，字号，...)
字体：0 1 2 3 4 5 6 7 8 9 ...16
'''

import numpy as np

import cv2
# zeros坐标代表：[y,x]
img = np.zeros((600, 600, 3), np.uint8)
# line 坐标代表：[x,y]
# 10 是线的宽度， 4是带锯齿的线，默认是8 ，可选值由   -1 4 8 16
cv2.line(img, (10, 30), (100, 300), (255, 255, 255), 10, 4)
# 画矩形
cv2.rectangle(img, (10, 10), (100, 100), (255, 255, 255), -1)
# 画圆形
cv2.circle(img, (320, 240), 100, (255, 255, 255))
cv2.circle(img, (320, 240), 5, (255, 255, 255), -1)
# 画椭圆 -1 填充
cv2.ellipse(img, (120, 180), (60, 100), 50, 0, 180, (255, 255, 255), -1)
# 画多边形
# 点集合
pts = np.array([(300, 10), (150, 100), (450, 100)], np.int32)
# 画边
cv2.polylines(img, [pts], True, (0, 255, 255))
# 填充
cv2.fillPoly(img, [pts], (255, 255, 0))

# 画文本
cv2.putText(img, 'English ...', (60, 60),
            cv2.FONT_ITALIC, 3, (255, 255, 255))


cv2.imshow('draw', img)
cv2.waitKey(0)
