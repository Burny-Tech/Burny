# Numpy
# OpenCV中用到的矩阵都要换换成Numpy的数组

# Numpy 基本操作

# 操作图片相当于操作矩阵
# 创建矩阵
# 检索与赋值[y , x]
# 获取子数组 [ :,:]

# 创建数组 array()
# 创建全0数组  zeros()/ones
# 创建全指数组 full()
# 创建单元数组  identity/eye() 正方形/非正方形

import cv2
import numpy as np

# 一维数组
a = np.array([2, 3, 4])
# 二维数组
c = np.array([[1, 2], [3, 4]])

print(a, '\n', c)

d = np.zeros((4, 8, 6), np.uint8)
# 行的个数，列的个数，通道数/层数  y, x 对于RGB 来说是有3个通道的
# np.unit8 矩阵中的数据类型 ，最大值为255

print(d)

f = np.ones((4, 8, 6), np.uint8)
print(f)

e = np.full((4, 8, 6), 255, np.uint8)
print(e)

# 单位矩阵
g = np.identity(3)
print(g)

# 非单位矩阵 k 从第2 个开始
s = np.eye(3, 6, k=2)
print(s)

# Numpy 基本操作

'''
创建矩阵
检索与赋值[y,x]
从 0 开始 ，注意和常见的[x,y] 有所区别
[y,x,channel] channel 通道数,对于彩色图像来说是3层的,灰色是1层的
获取子数组[:,:]
'''
# 全部是0 的3 层矩阵

img = np.zeros((480, 640, 3), np.uint8)

# 检索式3层的
print(img[100][100])

count = 0


while count < 200:
    # 检索一：
    # BGR B 的 255
    img[count, 100] = 255
    # 0 BGR 的B
    img[count, 100, 0] = 255
    # 1 BGR 的G
    img[count, 100, 1] = 255
    count = count + 1
    # 如果3层都是255 ，则是白色

    # 检索二：
    # BGR 分别为 0 0 255
    img[count, 100] = [0, 0, 255]

# ROI 操作
roi = img[100:200, 100:200]
# BGR 设置为红色
roi[:, :] = [0, 0, 255]

# cv2.imshow('img', img)
cv2.imshow('img', roi)
key = cv2.waitKey(0)
if key & 0xFF == ord('q'):
    cv2.destroyAllWindows()


# 矩阵操作3 ROI
'''
[y1:y2,x1:x2] 获取子矩阵
[:,:]获取矩阵的整个矩阵
'''
