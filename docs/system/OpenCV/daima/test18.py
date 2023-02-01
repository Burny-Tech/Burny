
import cv2
import numpy as np

'''
外接矩阵

最大外接矩阵

最小外接矩阵
('./public/images/026-最大最小外接矩阵.png')

minAreaRect(points)

points:轮廓
返回值
RotatedRect  : 是一个结构体，旋转的矩阵，其中的角度非常关键 其中包括

x,y 起始点
width,height
angle：角度

boundingRect(array)
array:轮廓
返回值： Rect
x,y 起始点

width,height 
'''

hand = cv2.imread('./public/images/027-waijiejuzhen.png')

hand_gray = cv2.cvtColor(hand, cv2.COLOR_BGR2GRAY)

hand_ret, hand_bin = cv2.threshold(hand_gray, 150, 255, cv2.THRESH_BINARY)


hand_con, hand_hierarchy = cv2.findContours(
    hand_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

r = cv2.minAreaRect(hand_con[1])


box = cv2.boxPoints(r)
box = np.int0(box)
cv2.drawContours(hand, [box], 0, (255, 255, 255), 2)

x, y, w, h = cv2.boundingRect(hand_con[1])
cv2.rectangle(hand, (x, y), (x+w, y+h), (255, 255, 0), 2)

cv2.imshow('hand', hand)

cv2.waitKey(0)
