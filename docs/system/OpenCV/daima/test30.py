'''
MeanShift 原理
严格来说该方法并不是用来对图像分割的,而是在色彩层面的平滑滤波
它会中和色彩分布相近的颜色,平滑色彩细节,侵蚀掉面积较小的颜色区域
它以图像上任一点P为圆心,半径为sp ,色彩幅值 sr 进行不断的迭代
sr 越大     对判断颜色相同的差异要求越低,准确率越低
sr 越小     对判断颜色相同的差异要求越高,准确率越高

('./public/images/054-图像分割-MeanShift 效果图.png')

API

pyrMeanShiftFiltering(img,double sp ,double sr ,maxLevel = 1)
maxLevel 默认值





'''

import cv2
import numpy as np

# img = cv2.imread('./public/images/youke.jpg')
img = cv2.imread('./public/images/coins.webp')


sp = 20

sr = 30

mean_img = cv2.pyrMeanShiftFiltering(img, sp, sr, 1)

# 之前有介绍过的Canny算法,寻找边缘
img_canny = cv2.Canny(mean_img, 150, 300)

# 分割出来的所有区域,第二个参数为所有区域的层级关系
contours, _ = cv2.findContours(
    img_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (255, 255, 255), 2)

cv2.imshow('img', img)

cv2.imshow('mean', mean_img)

cv2.imshow('imgc', img_canny)

cv2.waitKey()
