# 视频录制


# VideoWriter
# 参数一为 输出文件，参数二：指定多媒体文件格式（VidwoWriter_fourcc）参数三： 帧率，参数四：分辨率(查看电脑的摄像头的分辨率是多少进行设置)
# write
# release


# 视频采集


# VideoCapure() 虚拟采集器，采取第一个设备号
# cap.read() 将视频帧读取为图片帧
# cap.release() 释放资源

import cv2

fourcc = cv2.VideoWriter_fourcc(*'MJPG')

vw = cv2.VideoWriter('./out.mp4', fourcc, 25, (640, 360))


cv2.namedWindow('video', cv2.WINDOW_NORMAL)


# 0 代表的是第一个视频设备
# 或者改为视频文件所在的路径，即可更改为从视频文件中读取。
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 从摄像头获取视频帧 第一个:  为状态值，读到帧 为true 第二个为视频帧
    ret, frame = cap.read()
    if (ret):
        cv2.imshow('video', frame)
        vw.write(frame)
        # 等待10ms而已。
        key = cv2.waitKey(1)
        if (key & 0xFF == ord('q')):
            break
        else:
            print(key)
    else:
        break


cap.release()
vw.release()
cv2.destroyAllWindows()
