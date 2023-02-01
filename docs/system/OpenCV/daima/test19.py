# 车辆识别
'''
加载视频
通过形态学识别车辆
对车辆进行统计
显示车辆统计信息


去背景

createBackgroundSubtractorMOG(...)
history = 200

预存 多少位帧 有可以判断作为背景

python -m pip install opencv-contrib-python --user

'''

import cv2
import numpy as np

bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()


# 所有帧
cap = cv2.VideoCapture('./public/vedio/che.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 视频是 （frame）
line_hight = 380
offsert = 6
cars = []
carno = 0

# 计算中心点


def center(x, y, w, h):
    x1 = int(w/2)
    y1 = int(h/2)
    cx = x+x1
    cy = y + y1
    return cx, cy


while True:
    ret, frame = cap.read()
    if (ret):
        # print(frame.shape)
        # 灰度化
        huidu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 高斯去噪
        blur = cv2.GaussianBlur(huidu, (5, 5), 5)
        # 去背景
        mask = bgsubmog.apply(blur)
        # 形态学处理 腐蚀：去掉大物块 外的小物块
        erode = cv2.erode(mask, kernel)

        # 形态学处理 膨胀,恢复大小
        dilate = cv2.dilate(erode, kernel, iterations=3)

        # 闭运算去掉物体内部的小块

        close = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, kernel)

        # 查找轮廓
        # 所有轮廓，轮廓的关系
        con, cengji = cv2.findContours(
            close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.line(frame, (10, line_hight),
                 (480, line_hight), (255, 255, 255), 3)
        for (i, c) in enumerate(con):
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h),
                          (255, 255, 255), 2)
            # 如果> 25 才统计，这个需要加以调节
            if (w > 25 and h > 25):
                cpoint = center(x, y, w, h)
                cars.append(cpoint)
                for (x, y) in cars:
                    # 要有一条线
                    # 线有范围 6 ，上下6个像素点
                    # 从数组种减去
                    if ((y > line_hight - offsert) and (y < line_hight+offsert)):
                        carno += 1
                        cars.remove((x, y))
                        print(carno)

        cv2.putText(frame, "Cars Count:"+str(carno), (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
      #  cv2.imshow('huidu', huidu)
      #  cv2.imshow('blur', blur)
     #   cv2.imshow('mask', mask)
     #   cv2.imshow('erode', erode)
       # cv2.imshow('dilate', dilate)
       # cv2.imshow('close', close)
        cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if (key == 27):
        break


cap.release()
cv2.destroyAllWindows()
