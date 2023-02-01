# FLANN 特征匹配

'''
在进行批量特征匹配时,FLANN速读更快
由于它使用的邻近近似值,所以精度较差

使用步骤

* 创建FLANN匹配器,FlannBasedMather(index_params)
    index_params 字典:匹配算法KDTREE, LSH
        kdtree 适用于 SIFT算法 SURF 算法
        lsh  适用于orb算法
    如果是KDTREE 算法,还需要设置 search_params 字典:经验值:一般为index_params 的10倍 
    
    KDTREE : index_params = dict( algorithm = FLANN_INDEX_KDTREE,trees = 5)  FLANN_INDEX_KDTREE 实际就是1
    search_params = dict (checks = 50 )
    

* 进行特征匹配 flann.match/knnMatch()
    knnMatch(param1,param2)
    参数为SIFT SURF ORB 等计算的描述子
    k 表示取欧式举例最近的前k个关键字
    返回的是一个DMatch对象
        distance: 描述子之间的举例,值越低越好
        queryIdx 第一个图像的描述子索引值
        trainIdx 第二个图的描述子索引值
        imgIdx 第二图的索引值

* 绘制匹配点 cv2.drawMathes/drawMatchesKnn(...)

   drawMathesKnn
      搜索img ,kp
      匹配图像img ,kp
      match()方法返回的匹配结果
      

'''


import cv2
import numpy as np


# 打开两个文件
img1 = cv2.imread('./public/images/zheng.png')
img2 = cv2.imread('./public/images/zheng.png')

# 创建特征检测器

sift = cv2.SIFT_create()

# 灰度化
g1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
g2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


kp1, des1 = sift.detectAndCompute(g1, None)
kp2, des2 = sift.detectAndCompute(g2, None)

# 创建匹配器
index_params = dict(algorithm=1, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# 对描述子进行匹配计算
matches = flann.knnMatch(des1, des2, k=2)

good = []
for i, (m, n) in enumerate(matches):
    # 越小,近似度越高
    if m.distance < 0.7 * n.distance:
        good.append(m)


ret = cv2.drawMatchesKnn(img1, kp1, img2, kp2, [good], None)

cv2.imshow('re', ret)
cv2.waitKey(0)
