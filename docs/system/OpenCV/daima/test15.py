# 图像滤波
'''
一幅图像通过滤波器得到另一幅图像；
其中滤波器又称为卷积核，滤波的过程称为卷积

对图像进行扫描和乘法
卷积：原始图像与矩阵进行乘法运算

卷积的几个概念

卷积核的大小
锚点
边界扩充
步长

![]('./public/images/lvbo001.png')
![]('./public/images/lvbo002.png')

卷积核

卷积核一般为奇数，如3x3、5x5、7x7 等
一方面是增加padding的原因；
另一方面是保证锚点在中间，防止位置发生偏移的原因

卷积核大小的影响
在深度学习种，卷积核越大，看到的信息（感受野）越多
提取的特征越好，同时计算量也就越大

锚点
卷积核的正中心就是锚点
![]('./public/images/lvbo003.png')

边界扩充
当卷积核大于1 且不进行边界扩充，输出尺寸将相应缩小
当卷积核以标准方式进行边界扩充，则输出数据的空间尺寸将与输入相等

N = ( W - F +2P)/S +1
N 输出图像大小
W 源图大小
F 卷积核大小
P 扩充尺寸
S 步长大小，默认是1

低通滤波 和高通滤波

低通滤波可以去除噪音或平滑图像
高通滤波可以帮助查找图像的边缘，进行物体识别

图像卷积
filter2D(src,ddepth,kernel,anchor,delta,borderType)
ddepth:位深 ，当值为-1  的时候，表示输出的位深和输入的位深是一致的
kernel：卷积核 当卷积为低通滤波 ,当卷积为高通滤波,
anchor :锚点: 当值为-1 时候,则是输入的核对应的标准锚点
delta: 当卷积之后,可以相加的值,一般为0
borderType :边缘
'''
import cv2
import numpy as np


img = cv2.imread('./public/images/zheng.png')

# 5 x5 的矩阵,里面每个元素乘以 25分之一
kernel = np.ones((5, 5), np.float32) / 25

dst = cv2.filter2D(img, -1, kernel)

cv2.imshow('dst', dst)

'''
方盒滤波和均值滤波
这两种滤波器的卷积核是固定的.
('./public/images/001-方盒滤波卷积核.png')
参数a 是未知数

normalize = true , a = 1/W * H  均值滤波
normalize = false ,a = 1

当normalize == true 时, 方盒滤波 =平均滤波
一般取 normalize = true ,即方盒滤波一般是指 平均滤波

所以一般都是调用平均滤波的API

方盒滤波API
boxFilter(src ,ddepth,ksize,anchor,normalize,borderType)
#参数 原图,位深,卷积核大小,锚点,正常是否,边缘
当normalize =true时
均值滤波API
blur(src,ksize,anchor,borderType)
'''
fanghe = cv2.blur(img, (5, 5))

cv2.imshow('fanghe', fanghe)
'''
高斯滤波
('./public/images/002-高斯滤波.png')
('./public/images/003-高斯滤波.png')
('./public/images/004-高斯滤波.png')
中间权重大,旁边权重低
对高斯噪音进行处理

GaussianBlur ( img, kernel,sigmaX ,sigmaY...)
参数,原图,卷积核,
X,Y:最大范围到中心点有多少误差
('./public/images/005-高斯滤波.png')
https://blog.csdn.net/u013066730/article/details/123112159
'''

gaosi = cv2.GaussianBlur(img, (5, 5), sigmaX=1, sigmaY=1)
cv2.imshow('gaosi', gaosi)

'''
中值滤波
假设有一个数组[1556789],取其中的中间值作为卷积后的结果值
中值滤波的优点是对胡椒噪音效果明显(没错,就是胡椒噪音)

medianBlur(img,ksize)
'''
zhngzhi = cv2.imread('./public/images/006.png')


result = cv2.medianBlur(zhngzhi, 5)
cv2.imshow('zhngzhi', zhngzhi)
cv2.imshow('result', result)

'''
双边滤波
可以保留边缘,同时对边缘内的区域进行平滑处理
作用是进行美颜
之前的滤波不仅对图像区域误内无差别的处理,对边缘也处理.
('./public/images/007-双边滤波.png')

bilateralFilter(img,d,sigmaColor,sigmaSpace)
d: 直径


'''
shuangbian = cv2.bilateralFilter(img, 7, 20, 50)

cv2.imshow('shuangbian', shuangbian)


'''
高通滤波
常见的高通滤波

Sobel(索贝尔)-对噪音过滤很强,效果差,对边缘检测,只能求一个方向的边缘
Scharr(沙尔)-不可改变卷积核大小(3x3) 效果好,对边缘不可检测,只能求一个方向的边缘
Laplacian(拉普拉斯) ,能自己计算两个方向的边缘,但是没有降噪的功能


Solbel 算子

先向x方向求导
再向y方向求导
最终结果: |G| =|Gx|+|Gy|

Sobel(src,ddepth,dx,dy,ksize = 5,scale =1,delta = 0 ,borderType = Border_default)
当ksize = 3 ,则退化为沙尔
dx ,dy 只能设置其中一个为1,另外一个为0
当dx设置为1 时候,求的是对Y轴进行求导,算的是Y轴的边缘
当dy设置为1 时候,求的是对X轴进行求导,算的是X轴的边缘
scale :缩放比例

'''

sobel_old = cv2.imread('./public/images/008.png')
sobel1 = cv2.Sobel(sobel_old, -1, 1, 0, ksize=5)
sobel2 = cv2.Sobel(sobel_old, -1, 0, 1, ksize=5)
cv2.imshow('sobel1', sobel1)
cv2.imshow('sobel2', sobel2)

cv2.imshow('sobel', cv2.add(sobel2, sobel1))

'''
Scharr 沙尔算子

与Sobel类似,只不过使用的kernel值不同,kernel只支持3x3
Scharr只能求x方向或y方向的边缘
可以将更细小的线给识别出来
很少运用
Scharr(src,ddepth,dx,dy,)
'''

'''
Laplacian(拉普拉斯) 算子

缺点:对噪音敏感,一般需要先进行去噪再调用拉普拉斯算子
可以同时求两个方向
Laplacian(img,ddepth,ksize,scale=1,borderType =BORDER_DEFAULT)
'''

lap = cv2.Laplacian(sobel_old, -1)

cv2.imshow('lap', lap)

'''
边缘检测,终极大法

Canny
使用5x5高斯滤波消除噪音
计算图像梯度(0° 45 90 135)
取局部最大值
('./public/images/009-Canny阈值计算.png')

API
Canny(img,minVal,maxVal)

minVal maxVal:
min 越小:边缘越少 
max 只要超过最大值,都会认为是边缘,所以,max设置得越小,边缘会越多
min-max 之间的过大,则边缘会越少

'''

canny = cv2.Canny(sobel_old, 100, 200)
cv2.imshow('canny', canny)

cv2.waitKey(0)
