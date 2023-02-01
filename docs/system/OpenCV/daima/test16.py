# 形态学处理
'''
基于图像形态进行处理的一些基本方法
这些处理方法基本是对二进制图像进行处理(黑白图像进行处理)
卷积核决定着图像处理后的效果

形态学图像处理

腐蚀:形态缩小
膨胀:形态放大

开运算:先腐蚀,后膨胀
闭运算:先膨胀,后腐蚀

顶帽:
黑帽:

'''

'''
图像二值化(黑白处理)

将图像中的每个像素变成两种值:如0,255

二值化有两种

全局二值化
局部二值化

threshod (img ,thresh,maxVal ,type)
img :图像:最好是灰度图

超过阈值的时候,便是 黑色的点
thresh:阈值 ,低于阈值,则是为0 .高于阈值,则变成maxVal
maxVal: 超过阈值,替换成 maxVal

type: thresh_binary 和 thresh_binary_inv 
thresh_trunc
thresh_tozero 和thresh_tozero_inv

'''

import cv2
import numpy as np
img = cv2.imread('./public/images/zheng.png')
# 生成灰度图片
huidu = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 结果,以及输出的图像
ret, dst = cv2.threshold(huidu, 180, 255, cv2.THRESH_BINARY)

cv2.imshow('quan', dst)

'''
自适应阈值
解决全局二值化的缺点:由于光照不均匀以及阴影的存在,,只有一个阈值会使得在阴影处的白色被二值化成黑色

adaptiveThreshold(img,maxVal,adaptiveMethod,Type,blockSize,C)
method:计算阈值的方法
ADAPTIVE_THRESH_MEAN_C :计算邻近区域的平均值
ADAPTIVE_THRESH_GUASSIAN_C 高斯窗口加权平均值 常用

type:thresh-binary 或 thresh-binary_inv

blockSize:自定义区域大小
C 常量,应从计算出的平均值或加权平均值中减去

'''

zishiying = cv2.adaptiveThreshold(
    huidu, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 0)

cv2.imshow('zishiying', zishiying)

'''

2、膨胀（dilate）
膨胀就是求局部最大值的操作。从数学角度来说，就是将图像与核进行卷积，计算核B覆盖区域的像素点的最大值，并把这个最大值赋值给参考点指定的元素。这样就会使图像中的高亮区域逐渐增长。

3、腐蚀（erode）
腐蚀和膨胀是相反的操作，腐蚀是求局部最小值的操作。腐蚀操作会使图像中的高亮区逐渐减小。


腐蚀:苹果腐蚀
腐蚀的卷积核都是为1的矩阵

erode(img,kernel,iterations=1)
iterations: 腐蚀的次数

只有两者（黑底白图和卷积核）都是白色的时候，才能编程白色


'''
kernel = np.ones((3, 3), np.uint8)
fushi = cv2.erode(huidu, kernel, 9999)
cv2.imshow('fushi', fushi)

'''
形态学的卷积核
卷积核的类型
getStructuringElement(type,size)
type:Morph_rect ，矩形的，全1
Morph_ellipse 椭圆的矩阵，1组成一个圆形，其他为0
Morph_cross ：十字架 的矩阵，中间一列和中间一行是1 ，其他都是0 
size: (3,3)、(5,5)

'''
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
kernel4 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

print(kernel2)
print(kernel3)
print(kernel4)

'''
膨胀
卷积核越大，膨胀越大
只要有1 ，就能扩展。
dilate(img,kernel,iterations=1)
'''
r = cv2.dilate(huidu, cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)))

cv2.imshow('r', r)

'''
开运算=腐蚀+膨胀 (作用:腐蚀:先去除噪点,膨胀:恢复因去除噪点造成的损失)
闭运算=膨胀+腐蚀(作用:膨胀:先去除噪点,腐蚀:再恢复因去除噪点造成的损失)


开运算API 消除外部噪点 ，噪点越大，kernel越大
morphologyEx(img,MORPH_OPEN,KERNEL)
闭运算API
('./public/images/015-开运算-消除白噪点.png')
('./public/images/016-闭运算-消除白噪点.png')
消除白底的黑色噪点
morphologyEx(img,MORPH_CLOSE,KERNEL)

'''
kai = cv2.morphologyEx(huidu, cv2.MORPH_OPEN, kernel=kernel)
BI = cv2.morphologyEx(huidu, cv2.MORPH_CLOSE, kernel=kernel)


cv2.imshow('kai', kai)
cv2.imshow('BI', BI)

'''
形态学梯度
梯度 = 原图 - 腐蚀性
morphologyEx(img,MORPH_GRADIENT,kernel)
求：边缘
kernel比较大，腐蚀性比较大。边缘就不是特别清楚

'''
xingtaixue = cv2.morphologyEx(huidu, cv2.MORPH_GRADIENT, kernel=kernel)

cv2.imshow('xing', xingtaixue)


'''
顶帽运算
顶帽 = 原图 -  开运算
morphologyEx(img,MORPH_TOPHAT,kernel)
剩下黑底白色噪点
'''
ding = cv2.morphologyEx(huidu, cv2.MORPH_TOPHAT, kernel=kernel)

cv2.imshow('ding', ding)


'''
黑帽操作
黑帽 = 原图 -  闭运算
剩下白底的黑点
'''
h = cv2.morphologyEx(huidu, cv2.MORPH_BLACKHAT, kernel=kernel)

cv2.imshow('h', h)


'''
总结：
开运算，先腐蚀再膨胀，去除大图形外的小图形
闭运算：先膨胀再腐蚀，去除大图形内的小图形
梯度：求图形的边缘
顶帽：原图-开运算，得到大图形外的小图形
黑帽：原图-闭运算，得到大图形内的小图形


'''
cv2.waitKey(0)
