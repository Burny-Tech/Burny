# 图像变换

'''
图像的缩放
图像翻转
图像旋转
'''
'''
改变的是窗口内图像的大小
resize(src,dst,dsize,fx,fy,interpolation)
x轴的缩放因子
y轴的缩放因子
定义了dsize，就不需要定义fx fy
interpolation: 插值算法
Inter_nearest : 邻近插值，速度快，效果差
inter_linear : 双线性插值，原图中的4个点，默认算法
inter_cubic ：三次插值，原图中的16个点，但是花费时间比较长
inter_area :效果最好，但是时间较长
'''


import cv2
import numpy as np
img = cv2.imread('./public/images/zheng.png')
# 缩放0.5 倍
new = cv2.resize(img, (int(
    img.shape[1] * 0.5), int(img.shape[0] * 0.5)), None, interpolation=cv2.INTER_AREA)

cv2.imshow('new', new)


'''
图像反转
flip(img,flipCode)
0 上下翻转
> 0 左右翻转
<0 上下+左右翻转
'''
fanzhuan = cv2.flip(new, 2)
cv2.imshow('fanzhuan', fanzhuan)
'''
图像旋转
rotate(img,rotateCode)
顺时针90度  180度旋转  逆时针90度
ROTATE_90_CLOCKWISE
ROTATE_180
ROTATE_90_COUNTERCLOCKWISE
'''
xuanzhuan = cv2.rotate(new, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('xuanzhuan', xuanzhuan)

'''
图像的仿射变换 
仿射变换是图像旋转、旋转、平移的总称
warpAffine(src,M,dsize,flags,mode,value)
M: 变换矩阵(重要)
dsize:变换后的大小
flags: 与resize中的插值算法一致 （一般采用默认值）
mode: 边界外推法标志 （一般采用默认值）
value: 填充边界的值（一般采用默认值）
'''

'''
平移矩阵
矩阵中的每个元素由（x,y） 组成
如果是横向平移，则是在 x上增加数
如果是纵向平移，则是在 y 上增加数
因此，其变换矩阵是 2x2 的矩阵
平移向量为2x1 的向量，所在平移矩阵为2x3矩阵
6:56
'''
'''
https://blog.csdn.net/lz0499/article/details/90578545
说明：[[1,0],[0,1]] 表示 一个 2x2的单元矩阵。100，200表示偏移量，表示x 和 y的偏移量
'''

M = np.float32([[1, 0, 100], [0, 1, 200]])
h, w, ch = new.shape
pingyi = cv2.warpAffine(new, M, (w, h))

cv2.imshow('pingyi', pingyi)


'''
变换矩阵
getRotationMatrix2D(center,angle,scale)
获取矩阵M ，而不需要自己去计算
center 中心点
angle 角度-按逆时针 
scale 缩放比例

'''

# 这里只是图像内的大小，画布大小不变
M2 = cv2.getRotationMatrix2D((w/2, h/2), 45, 0.75)
print(M2)
# 如果想改变信画布的尺寸，需要更改dsize
bianhuan = cv2.warpAffine(new, M2, (w, h))
cv2.imshow('bianhuan', bianhuan)

'''
第二中变换矩阵
由直角三角形的三个点获得的新的变换矩阵
getAffineTransform(src[],dst[])

'''
src = np.float32([[40, 30], [80, 30], [40, 30]])
dst = np.float32([[20, 40], [60, 50], [15, 30]])
bianhuan2 = cv2.getAffineTransform(src, dst)

cv2.imshow('bianhuan2', bianhuan2)

'''
透视变换
将一种坐标系变换为另一种坐标系
warpPerspective(img,M,dsize)
M 是变换矩阵
dsize是目标图像的大小
# 获取M ， src dst 分别为四个点
getPersectiveTransform(src,dst)
'''
src = np.float32([[100, 110], [150, 160], [0, 50], [600, 800]])
dst = np.float32([[60, 80], [200, 250], [50, 100], [699, 899]])

M3 = cv2.getPerspectiveTransform(src, dst)
toushi = cv2.warpPerspective(new, M3, (w, h))
cv2.imshow('toushi', toushi)

cv2.waitKey(0)
