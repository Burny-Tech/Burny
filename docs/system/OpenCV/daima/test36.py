'''
Harr+Tesseract 车牌识别

Harr能定位到车牌的大体位置.
tesseract 提取数字


]步骤
通过Harr定位车牌的大体位置
对车牌进行预处理
调用tesseract进行文字识别

车牌预处理包括的内容
对车牌进行二值化处理
进行形态学处理
滤波去除噪点
缩放

Tesseract的安装

(https://blog.csdn.net/LOVEmy134611/article/details/119344846)



'''

import cv2

import numpy as np

import pytesseract as py

plate = cv2.CascadeClassifier('')

# 带车牌的图片
img = cv2.imread('./')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 检测车牌的位置

faces = plate.detectMultiScale(gray, 1.1, 3)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)


# 对获取到的车牌进行预处理,

# 提取ROI

roi = gray[y:y+h, x:x+w]

# 进行二值化

ret, roi_bin = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# 多个语言时,中间用加号

result = py.image_to_string(roi, lang='chi_sim+eng', config='--psm 8 --oem 3')

print(result)
cv2.imshow('roi_bin', roi_bin)

cv2.imshow('img', img)
cv2.waitKey
