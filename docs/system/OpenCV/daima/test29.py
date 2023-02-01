# GrabCut 法- 前后景分离
'''
通过交互的方式(鼠标)获取前景物体.

* 用户指定前景的大体区域,剩下的为背景区域.
* 用户还可以明确指定某些地方为前景或背景
* GrabCut采用分段迭代的方法分析前景物体形成模型树
* 最后根据权重决定某个像素是前景还是背景

[示例]GrabCut

* 主体结构
* 鼠标事件的处理
* 调用GrabCut实现前景和背景的分离

GrabCut API 
grabCut(img,,mask,bgdModel,fgdModel,iterrator,mode)

mask: 进行分割之后产生的掩码是多少.得到掩码后,就能将要分割的图片摘取出来.每一个像素值的含义都能了解到
rect: 图片选取的区域
bgdModel:固定值
fgdModel:固定值
iterator ;迭代次数

mask:
BGD 背景 0
FGD 前景  1
PR_BGD 可能是背景 2
PR_FGD 可能是背景 3 

bgdModel  是 np.float64 type zero arrays of size(1,65) 64位的浮点型
fgdModel 同上

mode

GC_INIT_WITH_RECT : 指定区域找前景
GC_INIT_WITH_MASK :第一次调用  GC_INIT_WITH_RECT 对前后景进行分离,之后还可以通过  GC_INIT_WITH_MASK 进行迭代

'''

import cv2

import numpy as np

# 定义一个类,用户对象的数据共享


class App:

    startX = 0
    startY = 0
    rect = (0, 0, 0, 0)

    flag_rect = False

    def onmouse(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.flag_rect = True
            self.startX = x
            self.startY = y
            print('左键下')
        elif event == cv2.EVENT_LBUTTONUP:
            cv2.rectangle(self.img, (self.startX, self.startY),
                          (x, y), (255, 255, 255), 3)
            self.flag_rect = False
            self.rect = (min(self.startX, x), min(self.startY, y),
                         abs(self.startX - x), abs(self.startY - y))
            print('左键上')
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.flag_rect == True:
                # 关键代码,每次都是拿一个新的img进行绘制
                self.img = self.img2.copy()
                cv2.rectangle(self.img, (self.startX, self.startY),
                              (x, y), (0, 255, 0), 3)
            print('鼠标挪动')

    def run(self):
        print('self')
        cv2.namedWindow('input')
        cv2.setMouseCallback('input', self.onmouse)

        self.img = cv2.imread('./public/images/youke.jpg')
        self.img2 = self.img.copy()
        # 掩码只有一层,所有只需要shape的前两个参数
        self.mask = np.zeros(self.img.shape[:2], dtype=np.uint8)
        self.output = np.zeros(self.img.shape, np.uint8)

        while (1):
            cv2.imshow('input', self.img)
            cv2.imshow('self', self.output)
            k = cv2.waitKey(100)
            if k == 27:
                break
            if k == ord('g'):
                bgdModel = np.zeros((1, 65), np.float64)
                fgdModel = np.zeros((1, 65), np.float64)
                cv2.grabCut(self.img2, self.mask,
                            self.rect, bgdModel, fgdModel, 1, cv2.GC_INIT_WITH_RECT)
                mask2 = np.where((self.mask == 1) | (
                    self.mask == 3), 255, 0).astype('uint8')
                self.output = cv2.bitwise_and(self.img2, self.img2, mask=mask2)


App().run()

# 画框之后摁 g
