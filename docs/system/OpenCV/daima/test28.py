# 图像分割

# 将前景物体从背景中分离出来

# 传统的图像分割方法

# 分水岭法
#   GrabCut法-ps抠图
#   MeanShift法
#   背景扣除
# 基于深度学习的图像分割方法


# 分水岭法
# 图像经过二值化后 纵轴表示 0 - 255 0 .黑点 255 白点
'''
('./public/images/045-分水岭法1.png')
('./public/images/046-分水岭法2.png')
('./public/images/047-分水岭法.png')

分水岭法的处理步骤
 * 标记背景
 * 标记前景
 * 标记未知区域
 * 进行分割

'''

# 实例: 分割硬币

'''
分水岭API

watershed(img,masker)
masker:包括前景标记,背景标记,未知区域

获取背景:
('./public/images/048-分割硬币-获取背景.png')
('./public/images/049-分割硬币-获取前景.png')
('./public/images/050-分割硬币-未知区域.png')


'''


# 获取背景
# 1. 通过二值法得到黑白图片
# 2. 通过形态学获取背景


import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('./public/images/coins.webp')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 0的位置   如果设置为100 最小值 超过100设置为白色,小于100 为黑色  白色为255,则不用 在  cv2.THRESH_BINARY  + cv2.THRESH_OTSU
# ret:执行结果成功与否 thresh:成功的图片
# thresh_otsu 自适应阈值,会将100设置为自适应的阈值.所以100的位置设置为0
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# 对硬币进行形态学处理,保证硬币是硬币,背景是背景
# 去除外部白色噪点

kernel = np.ones((3, 3), np.int8)
# 2是进行开运算两次
open1 = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, 2)

# 膨胀 获取背景物体
bg = cv2.dilate(open1, kernel, iterations=1)

# 距离变换API -计算非0值到离他最近的0值的距离，
#  distanceTransform(img,distanceType,maskSize)
#  distanceType: DIST_L1 、DIST_L2 ,一般用L2 ,即用勾股定理
#  (x1,y1) 非0值的坐标  （x2，y2） 0值的坐标
# L1 绝对值的计算  (|x1| - |x2|) + (|y1| - |y2|)
# L2   勾股定理
# maskSize 扫描的时候卷积核的大小，一般L1 用3 大小的卷积核  L2用 5 大小 的卷积核

# 连通域API
# 连通区域（Connected Component）一般是指图像中具有相同像素值且位置相邻的前景像素点组成的图像区域（Region，Blob）。
# 连通区域分析（Connected Component Analysis,Connected Component Labeling）是指将图像中的各个连通区域找出并标记。
# 连通区域分析是一种在CVPR和图像分析处理的众多应用领域中较为常用和基本的方法。
# 例如：OCR识别中字符分割提取（车牌识别、文本识别、字幕识别等）、视觉跟踪中的运动前景目标分割与提取（行人入侵检测、遗留物体检测、基于视觉的车辆检测与跟踪等）、
#            医学图像处理（感兴趣目标区域提取）、等等。也就是说，在需要将前景目标提取出来以便后续进行处理的应用场景中都能够用到连通区域分析方法，通常连通区域分析处理的对象是一张二值化后的图像。
# https://zhuanlan.zhihu.com/p/44702120
# connectedComponents(img,connectivity,...)
# 求图像中所有非0的连通域
# connectivity :4 8 (默认)
#  connectivity 个角点进行判断
#  4 :非0值的上下左右的四个点, 8 :非0值的上下左右以及四个角点


# cv2.imshow('thresh', thresh)

# cv2.imshow('bg', bg)

# 获取前景图

dist = cv2.distanceTransform(open1, cv2.DIST_L2, 5)

# imshow 显示梯度的时候效果不是很好,引用  matplotlib
# ('./public/images/051-连通域效果.png')
# cv2.imshow('dis', dist)
# plt.imshow(dist, cmap='gray',)
# plt.show()

ret2,  fg = cv2.threshold(dist, 0.7 * dist.max(), 255, 0)
# ('./public/images/052-分水岭法获取前景效果图.png')
# cv2.imshow('fg', fg)

# 获取未知区域  未知区域  = 背景 - 前景
unknow = cv2.subtract(bg, np.uint8(fg))
# cv2.imshow('unknow', unknow)

# 创建连通域
ret, marker = cv2.connectedComponents(np.uint8(fg))
#  将背景和位置区域都设置好 用1 代表 背景,对所有元素 +1 背景也+1 了.前景在原来的基础上+1 对前景没有区别
marker = marker + 1
# 未知区域全部为0
marker[unknow == 255] = 0


# 进行图像分割,所有的边缘用-1表示

result = cv2.watershed(img, marker)
# 将边缘设置为红色
img[result == -1] = [0, 0, 255]

('./public/images/053-分水岭分割最终效果图.png')
cv2.imshow('img', result)

cv2.waitKey()
