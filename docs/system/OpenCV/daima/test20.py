# OpenCV特征检测
'''
应用场景：
图像搜索，如以图搜图
拼图游戏
图像拼接，将两长有关联的图拼接到一起

拼图方法
* 寻找特征
* 特征是唯一的
* 可追踪的
* 能比较的
* 平坦部分很难找到它再原图中的位置
* 边缘相比平坦要号召一些，但也不能一下确定
* 角点可以一下就能找到其再原图中的位置

什么是特征

图像特征就是指有意义的图像区域，具有独特性，易于辨识性，比如角点，，斑点 以及高密度区

角点：
* 灰度梯度的最大值对应的像素
* 两条线的交点
* 极值点（一阶导数最大值，但二阶导数为0）

Harris角点
('./public/images/028-Harris.png')

* 光滑地区,无论向哪里移动,衡量系数不变
* 边缘地址,垂直边缘移动时,衡量系统变化剧烈
* 在焦点处,无论往哪个方向移动,衡量系统都变化剧烈
API
cornelHarris(img,blockSize,ksize,k)
blockSize:检测窗口大小
ksize:SObel卷积核
k:权重系系数,经验值,一般取0.02-0.01
返回值:
所有角点

'''
import cv2
import numpy as np

img = cv2.imread('./public/images/zheng.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
harris = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# img[harris > 0.01*harris.max()] = [0, 0, 255]
# cv2.imshow('img', img)
# ('./public/images/028-Harris效果图.png')

'''
Shi-Tomasi角点
* 对Harris角点加测的改进
* Harris 检测算的稳定性和K值有关,而K是个经验值,不好设定值
API
goodFeaturesToTrack(img,maxCorners,...)
maxCorners:角点的最大数,值为0 表示无限制
qualityLevel: 小于1.0的证书,一般在0.01-0.1之间
minDistance: 角之间最小欧式举例,忽略小于此距离的点
mask: 感兴趣的区域
blockSIze:检测窗口的大小
useHarrisDetector: 是否使用Harris算法,默认值为false,
k:默认是0.04

'''

corners = cv2.goodFeaturesToTrack(
    gray, maxCorners=1000, qualityLevel=0.01, minDistance=10)

corners = np.int0(corners)
for i in corners:
    # 多维转一维
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, (255, 255, 255), -1)

cv2.imshow('shi', img)


cv2.waitKey(0)
