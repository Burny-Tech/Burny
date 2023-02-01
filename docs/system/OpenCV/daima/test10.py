# OpenCV 重要的结构体Mat

# 矩阵 ，可以有多通道，如果是灰色的话，只有1 个通道， 如果是彩色的，则有3 个通道

# mat有什么好处，操作矩阵方便

# 底层实现： header   - > data
'''
class cv_exports mat{
    public:
      int dims: 维数
      int rows,cols ;行列数
      uchar * data; 存储数据的指针
      int *refcount; 引用计数
      depth: 像素的位数 ，彩色是8位数据
      size: 矩阵的大小
      channel: 通道数，RGB是3  
      type: dep+dt+chs CV_8UC3
      
}；
'''

# mat 深拷贝 浅拷贝
# 默认是属于 浅拷贝
# Mat A
# A = imread(file,IMAREAD_COLOR)
# Mat B(A)
# 深拷贝
'''
cv::Mat::clone() 
cv::Mat::copyTo()
copy() 接口 ，底层会调用上述的两个深拷贝接口
'''


import cv2
import numpy as np
img = cv2.imread('./public/images/zheng.png')

# 浅拷贝
img2 = img
img3 = img.copy()

img[10:100, 10:100] = [0, 0, 255]

cv2.imshow('img', img)
cv2.imshow('img2', img2)
# 深拷贝
cv2.imshow('img3', img3)
# cv2.waitKey(0)

# 图像的属性

# 高度 长度  通道数
print(img.shape)
# size = 高度 * 长度  * 通道数
print(img.size)
# 图片位深度
print(img.dtype)

# 通道的分离和合并

'''
split(mat)
merge((ch1,ch2,...))
'''

img4 = np.zeros((480, 360, 3), np.uint8)

cv2.imshow('img4', img4)

b, g, r = cv2.split(img4)
b[10:100, 10:100] = 255

cv2.imshow('b', b)

new = cv2.merge((b, g, r))
cv2.imshow('new', new)

cv2.waitKey(0)
