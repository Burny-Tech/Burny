'''
MOG2去背景
同MOG 类似,不过对亮度产生的阴影有更好的识别,缺点,产生噪点
API
createBackgroundSubtractorMOG2(
history,//500毫秒
...

detectShadows//是否检测阴影,默认为True

GMG去背景 
静态背景图像估计和每个像素的贝叶斯分割抗噪性更强
优点;可以计算阴影背景,去除噪点
缺点:采用默认值,则在开始好长时间内是黑屏,取决于帧率.

API:
cv2.createBackgroundSubtractorGMG(

initializationFrames ,//初始帧数,120,这和MOG MOG2 最大的区别

)

)
'''

import cv2
import numpy

# 从设备号中获取
cap = cv2.VideoCapture(0)

# mog = cv2.createBackgroundSubtractorMOG2()

mog = cv2.bgsegm.createBackgroundSubtractorGMG()


while (True):
    # ret: 结果 frame:一帧一帧的页面
    ret, frame = cap.read()
    # 掩码
    fgmask = mog.apply(frame)

    cv2.imshow('img2', frame)
    cv2.imshow('img', fgmask)

    k = cv2.waitKey(1)

    if k == 27:
        break

cap.release()
cv2.destroyAllWindows
