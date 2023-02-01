# 图像轮廓

# 什么是图像轮廓
# 具有相同颜色活泼强度的连续点的曲线
'''
图像轮廓的作用

可以用于图形分析
物体的识别和检测

注意点：
为了检测的准确性，需要先对图像进行二值化或Canny操作
画轮廓时会修改输入的图像

轮廓查找的API

findContours(img,mode,ApproximationMode...)

模式-mode：

Retr_external=0,表示之检测外轮廓
Retr_list=1,检测的轮廓不建立等级关系-常用
Retr_ccomp = 2 ,每层最多两级
Retr_tree = 3 ,按树形存储轮廓-常用
('./public/images/020-轮廓-EXTERNAL.png')
('./public/images/021-轮廓-LIST.png)
('./public/images/022-轮廓-CCOMP.png')
('./public/images/023-轮廓-TREE.png')

近似模式-ApproximationMode：

chain_approx_none :保存所有轮廓上的点
CHAIN_APPROX_SIMPLE 只保存角点

两个返回值：
contours 和hierarchy

contours:所有轮廓
hierarchy:轮廓间的层级关系

'''

'''
查找轮廓
'''

import cv2
origin = cv2.imread('./public/images/zheng.png')

cv2.imshow('origin', origin)
# 单通道
huidu = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)
cv2.imshow('huidu', huidu)

# 由3通道转换为单通道
print(origin.shape)
print(huidu.shape)

# 二值化
ret, binary = cv2.threshold(huidu, 150, 255, cv2.THRESH_BINARY)
cv2.imshow('bin', binary)

# 返回值：所有轮廓值，以及轮廓之间的关系
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contours, hierarchy)


# 如何绘制轮廓

'''
drawContours(img,contours,controurIdx,color,thickness)

contourIdx :设置顺序号， -1 表示绘制所有轮廓
color:轮廓颜色 
thicknes:线宽，-1 是全部填充

'''
# 可输入原图，或者二进制图，或者单通道图
new = cv2.drawContours(origin, contours, -1, (255, 255, 255), 1)

cv2.imshow('new', new)

'''
轮廓的面积和周长

contourArea(contour)
contour:轮廓

arcLength(curve,closed)
closed:是指闭合的还是非闭合的

'''

area = cv2.contourArea(contours[2])

print(area)
length = cv2.arcLength(contours[2], True)

print(length)


'''
多边形逼近与凸包
('./public/images/024-多边形逼近与凸包.png')

API

approxPolyDP(curve,epsilon,closed)
curve:轮廓
epsilion: 精度
closed:是否是闭合的轮廓

convexHull(points,clockwise,..)
clockwise:顺时针绘制

'''

hand = cv2.imread('./public/images/025-hand.png')

hand_gray = cv2.cvtColor(hand, cv2.COLOR_BGR2GRAY)

hand_ret, hand_bin = cv2.threshold(hand_gray, 150, 255, cv2.THRESH_BINARY)

hand_con, hand_hierarchy = cv2.findContours(
    hand_bin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hand_cond = cv2.drawContours(hand, hand_con, 0, (255, 255, 255), 1)
cv2.imshow('hand_cond', hand_cond)
print('hand_cond_len', hand_cond)

# 这里选取有问题
approx = cv2.approxPolyDP(hand_con[1], 20, True)


def drawShape(src, points):
    i = 0
    while i < len(points):
        if (i == len(points)-1):
            x, y = points[i][0]
            x1, y1 = points[0][0]
            cv2.line(src, (x, y), (x1, y1), (255, 255, 255), 1)
        else:
            x, y = points[i][0]
            x1, y1 = points[i+1][0]
            cv2.line(src, (x, y), (x1, y1), (255, 255, 255), 1)
        i = i+1


drawShape(hand, approx)

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


cv2.waitKey(0)
