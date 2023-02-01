# SIFT 关键点检测
'''
Scale-Invariant Feature Transform
与缩放无关的关键点检测

SIFT出现的原因
* Harris 角点具有旋转不变的特性
* 但缩放后就可能不再是关键点了

使用SIFT 步骤
创建SIFT对象
进行检测 ,kp=sift.detect(img,...)
绘制关键点,cv2.drawKeypoints(gray,kp,img)


'''

import cv2
import numpy as np
img = cv2.imread('./public/images/zheng.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


sift = cv2.SIFT_create()

# 第二个参数none代表整个区域检测
kp = sift.detect(gray, None)

cv2.drawKeypoints(gray, kp, img)

'''
计算SIFT 描述子

描述子和关键点的区别
关键点:位置,大小和方向
关键点描述子:记录了关键点周围对其有贡献的像素点的一组向量值,其不受仿射变换,光照变换影响

API:

des: 描述子 ,其作用是进行特征匹配
kp: 关键点 keypoints

kp, des = sift.compute(img,kp)

同时计算关键点和描述
kp ,des = sift.detectAndCompute(img,...)
mask:指明对img中哪个区域进行计算
'''
kp2, des2 = sift.detectAndCompute(gray, None)
print(des2)


cv2.imshow('img', img)
cv2.waitKey(0)
