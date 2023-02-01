# SURF特征检测
'''
Speeded-UP Robust Features
加速的鲁棒性
SIFT最大的问题是速度慢,因此才有SURF

使用SURF 的步骤

surf = cv2.xfeatures2d.SURF_create()
kp ,des = surf.detectAndCompute(img,mask)

'''

import cv2
import numpy as np

img = cv2.imread('./public/images/zheng.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 没有该接口此视频实战忽略.如有需要更换为SIFT接口

cv2.SURF

# 第二个参数none代表整个区域检测
kp = sift.detect(gray, None)

cv2.drawKeypoints(gray, kp, img)
