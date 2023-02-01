# 特征匹配方法
'''
BF: Brute-Force 暴力特征匹配方法
FLANN  最快邻近特征匹配方法

暴力特征匹配原理:它使用第一组中的每个特征的描述子,与第二组中的所有特征描述子进行匹配(枚举匹配) 计算他们之间的差距,然后将最近一个匹配返回

OpenCV特征匹配步骤

创建匹配器 BFMatcher  (normType,crossCheck )

normType 近似度算法 ,有以下几种
* NORM_L1  用于SIFT 和SURF
* NORM_L2 用于SIFT 和SURF ,默认值
* HAMMING1 用于ORB 算法
* HAMMING2 用于ORB算法

crossCheck 是否进行交叉匹配,默认为false ,开启后计算量会更大



进行特征匹配   bf.match (des1 ,des2 )
des:描述子

回执匹配点:cv2.drawMatches(img1,kp1,img2,kp2)

搜索图 img1 ,kp1
匹配图 img2  kp2

match() 方法返回匹配的结果


'''

import cv2
img1 = cv2.imread('./public/images/zheng.png')
img2 = cv2.imread('./public/images/zheng.png')

# 灰度化
g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
g2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# 创建sift
sift = cv2.SIFT_create()

kp1, des1 = sift.detectAndCompute(g1, None)
kp2, des2 = sift.detectAndCompute(g2, None)

bf = cv2.BFMatcher(cv2.NORM_L2)

match = bf.match(des1, des2)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, match, None)

cv2.imshow('img3', img3)

('./public/images/029-暴力特征匹配效果.png')


cv2.waitKey(0)
