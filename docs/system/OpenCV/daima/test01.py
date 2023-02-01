# https://www.bilibili.com/video/BV1Mv4y1M7gJ?p=118&spm_id_from=pageDriver&vd_source=010173c6f35c758e74dd6593e5722af0

import cv2

img = cv2.imread('./public/images/zheng.png')
cv2.imshow('img', img)
cv2.waitKey(0)


# 创建和显示窗口

# namedWindow()
# imshow()
# destroyAllWindows()
# resizeWindow

cv2.namedWindow('NEW', cv2.WINDOW_AUTOSIZE)
cv2.imshow('img', 0)
