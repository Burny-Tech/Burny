'''
图像修复

('./public/images/055-图像修复效果.png')

API

inpaint(
img,
mask,//与原始图片一样大小的,黑底白色的残缺位置的图片
inpaintRadius,//每个点的圆形领域半径
flags //INPAINT_NS INPAINT_TELEA
)

INPAINT_NS 


INPAINT_TELEA 算法简单,破损里的平方加权平均值

# 有点不是很智能,需要找到破损的图片
'''

import cv2

import numpy as np

img = cv2.imread('./public/images/coins.webp')

mask = cv2.imread('./public/images/coins.webp', 0)

dst = cv2.inpaint(img, mask, 5, cv2.INPAINT_TELEA)

cv2.imshow('dst', dst)
cv2.waitKey()
