'''
视频前后背景分离

视频背景扣除原理

* 视频是一组连续的帧(一幅幅图组成)
* 帧与帧之间关系密切,组成一组帧,称为 GOP
* 在GOP中,背景几乎是不变的

MOG去除背景
* 混合高斯模型为基础的前景/背景分割算法
* createBackgroundSubtractorMOG(
    history,//默认200ms 建立参考帧至少需要200ms
    nmixtures,//高斯范围值,默认为5 像素,把一个大的图片分成5x5的小块,每个5x5的小块都有一个高斯值,从而算出参考模型
    backgroundRatio,//背景比率,默认0.7 这张图中 70% 属于背景.
    nosiseSigma //默认0 自动降噪 
    
)

'''

import cv2
import numpy

# 从设备号中获取
cap = cv2.VideoCapture(0)

mog = cv2.createBackgroundSubtractorMOG2()


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
