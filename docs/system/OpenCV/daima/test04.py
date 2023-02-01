# 视频采集


# VideoCapure() 虚拟采集器，采取第一个设备号
# cap.read() 将视频帧读取为图片帧
# cap.release() 释放资源

import cv2


cv2.namedWindow('video', cv2.WINDOW_NORMAL)

# 0 代表的是第一个视频设备
# 或者改为视频文件所在的路径，即可更改为从视频文件中读取。
cap = cv2.VideoCapture(0)

while True:
    # 从摄像头获取视频帧 第一个:  为状态值，读到帧 为true 第二个为视频帧
    ret, frame = cap.read()
    cv2.imshow('video', frame)

    # 等待10ms而已。
    key = cv2.waitKey(1)
    if (key & 0xFF == ord('q')):
        break
    else:
        print(key)

cap.release()
cv2.destroyAllWindows()
