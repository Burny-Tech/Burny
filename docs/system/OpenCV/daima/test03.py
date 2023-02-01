# 保存图片

import cv2


# 创建和显示窗口

# namedWindow()
# imshow()
# destroyAllWindows()
# resizeWindow

cv2.namedWindow('NEW', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('NEW', 500, 500)

img = cv2.imread('./public/images/zheng.png')

while True:
    cv2.imshow('NEW', img)
    key = cv2.waitKey(0)
    # key 16 进制  获取了 8 进制  后与q的ASCII码进行比对
    if (key & 0xFF == ord('q')):
        break
    elif (key & 0xFF == ord('c')):
        cv2.imwrite('./public/images/write.png', img)
    else:
        print(key)
cv2.destroyAllWindows()
