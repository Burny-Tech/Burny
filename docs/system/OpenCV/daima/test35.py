'''
基本概念:
范围,互为包含关系
人工智能 > 机器学习 > 深度学习

计算机视觉与机器学习的关系

计算机视觉是机器学习的一种医用,而且是最有价值的应用

人脸识别

有两种主要的方法

哈儿级联方法(Harr) --cv自带的
深度学习方法(DNN)


哈儿级联法 

Harr是专门解决人脸识别而退出的
在深度学习还不流行的时候,Harr已可以商用.

Harr人脸识别步骤

创建Harr级联器
导入图片并将其灰度化
调用detectMultiScale方法进行人脸识别

detectMultiScale(img,
double scaleFactor =1.1  //缩放因子,哈儿级联器,对图片进行扫描,可能扫描的时候不能把人脸扫描进来,对图片进行缩小或进行放大.
int minNeighbors = 3  //最小的像素值,人脸识别的时候最少需要的像素
...

)

优缺点: 可以检测到正面的图片,但是侧面检测不到
'''

import cv2

import numpy as np

# 创建harr级联器

# 这里需要输入已经训练好的训练模型,需要识别脸的话就输入脸的模型,眼睛的的话就输入眼睛的模型
facer = cv2.CascadeClassifier()

# 导入人脸识别图片并将其灰度化
img = cv2.imread('')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 第三步,进行人脸识别
# [ [x,y,w,h]  ]
facer.detectMultiScale(gray, 1.1, 5)

for (x, y, w, h) in facer:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.imshow('img', img)

cv2.waitKey()
