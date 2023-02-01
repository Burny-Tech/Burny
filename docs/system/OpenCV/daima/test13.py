# 基本图像运算与处理
# 形态学
# 轮廓查找


# 图像的相加，相减 乘除
# 加：曝光更多， 减 曝光更少  乘 曝光比加更厉害  除  曝光比减更厉害
import cv2
import numpy as np

# 图形的运行 = 矩阵的运算
# 因此，加法运算的两张图必须是相等的

hsv0001 = cv2.imread('./public/images/HSV001.png')

print(hsv0001.shape)

img = np.ones((hsv0001.shape[0], hsv0001.shape[1], 3), np.uint8) * 50

result = cv2.add(hsv0001, img)
# 图像的减法
result2 = cv2.subtract(result, img)
result3 = cv2.multiply(hsv0001, img)
result4 = cv2.divide(hsv0001, img)


cv2.imshow('result2', result2)
cv2.imshow('result3', result3)

cv2.imshow('result4', result4)

cv2.imshow('origin', hsv0001)
cv2.imshow('result', result)


# 图像的溶合
# 只有两张图的属性是一样的才可以融合
'''
A 图像  B 图像
alpha beta 是权重
addWeighted(A ,alpha,B,bate,gamma)
gamma 静态权重
'''


i3 = cv2.addWeighted(hsv0001, 0.7, img, 0.3, 0)
cv2.imshow('i3', i3)

# 图像位运行

'''
没有进位

与 只有两个为1 结果才为1
或 只要由一个1 结果就为1
非 取反
异或 只有两个不一样才为1 不然为0 

'''

n1 = np.zeros((500, 500), np.uint8)

n1[200:300, 200:300] = 255
n2 = np.zeros((500, 500), np.uint8)

n2[250:350, 250:350] = 255

cv2.imshow('n1', n1)
cv2.imshow('n2', n2)

not_i = cv2.bitwise_not(n1)
and_i = cv2.bitwise_and(n1, n2)
or_i = cv2.bitwise_or(n1, n2)
xor_i = cv2.bitwise_xor(n1, n2)

cv2.imshow('not', not_i)
cv2.imshow('and', and_i)
cv2.imshow('or', or_i)
cv2.imshow('xor', xor_i)


cv2.waitKey(0)
