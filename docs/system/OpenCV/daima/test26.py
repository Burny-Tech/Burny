# 图像查找
'''
特征匹配+ 单应性矩阵

单应性矩阵 :透视变换
'''

# 打开两个文件
import cv2
import numpy as np


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


if len(good) >= 4:
    srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)

    # 获取单应性矩阵
    H, _ = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5.0)
    h, w = img1.shape[:2]
    pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]
                     ).reshape(-1, 1, 2)
    dst = cv2.perspectiveTransform(pts, H)
    cv2.polylines(img2, [np.int32(dst)], True, (0, 0, 255))
else:
    print('eror')
    exit()

ret = cv2.drawMatchesKnn(img1, kp1, img2, kp2, [good], None)

cv2.imshow('re', ret)
cv2.waitKey(0)
