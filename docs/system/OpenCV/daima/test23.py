# ORB 特征检测
'''
Oriented Fast And Rotated Brief
特征点检测与描述子

ORB优势:
ORB 可以做到实时检测

FAST特征点检测: 可以做到特征点的实时检测
brief:是对已检测到的特征点进行描述,它加快了特征描述符建立的速读,同时也极大降低了计算的速读

使用ORB步骤

orb = cv2.ORB_create()





'''

'''
总结:
SIFT :计算准确率最高,速读最慢,能检测出来的关键点和描述子最多欧

SURF:速读比SIFT,计算准确率比SIFT低
ORB:速读最快,能做到实时性,计算准确率最低 

'''


import cv2
import numpy as np
img = cv2.imread('./public/images/zheng.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 没有该接口此视频实战忽略.如有需要更换为SIFT接口

sift = cv2.ORB_create()

# 第二个参数none代表整个区域检测
kp, des = sift.detectAndCompute(gray, None)

cv2.drawKeypoints(gray, kp, img)

cv2.imshow('img', img)

cv2.waitKey(0)
