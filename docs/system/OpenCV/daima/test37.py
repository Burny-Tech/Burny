import cv2
from cv2 import dnn
import numpy as np
'''

* 什么是深度学习
* 几种常见的深度学习网络
* 构建深度学习网络的框架tf ,pytorch
* 进行网络训练的数据集

深度学习基础概念
深度学习是计算机视觉最为重要的方法

* 深度学习在40年代就被剔除,但一直停滞不前
* 2011,微软在语音识别上使用,取得了突破的效果
* 2012 ,DNN在图像识别领域取得惊人的效果,错误率从26% 降低到15%
* 2016 AlphaGo击败人类,引起世界震惊

深度学习网络模型

DNN(Deep Neural Network) 深度神经网络

RNN CNN 是属于一种特殊的DNN 

RNN(Recurrent Neural Network) 循环神经网络
CNN(Convolutional Neural Network) 卷积神经网络

RNN用途
* 语音识别
* 机器翻译
* 生成图像描述

CNN:
* 图片分类,检索
* 目标定位检测
* 目标分割
* 人脸识别

几种CNN网络实现
* LeNet 1998 第一代 28x28手写
* AlexNet 2012 ImageNet 比赛的冠军
* 还有这几种: VGG ,GoogleLeNet , ResNet

几种CNN目标检测网络实现
* RCNN ,FastRCNN ,Faster RCNN
* SSD
* YOLO  YOLOv2 ...  YOLOv5

深度学习库
* tensorflow ,google出品
* caffe -> caffe2 ->torch(pytorch)  贾扬清开源 ->facebook 提供
* MXNet Apache出品

训练数据集 -> 只有经过数据集训练 神经网络 才能成效

* MNIST Fashion-MNIST 手写字母
* VOC 举办挑战赛时的数据集 2012年后欧不再举办
* COCO 用于目标检测的大型数据集
*  ImageNet 

通过网络和数据集训练出来的模型称为训练模型

TF训练出的模型是 *.pb 文件
Pytorch 训练出的模型是 *.pth 文件
Caffe 训练处的模型是 .caff
ONNX 开放性神经网络交换格式 .onnx 

OpenCV 对DNN的支持



OpenCV 3.3 将DNN转正
OpenCV 只能使用DNN 不能训练DNN模型

OpenCV 支持的模型
* Tensorflow
* pytorch/torch
* caffe
* darknet


'''

'''
OpenCV使用DNN
DNN使用步骤

1. 读取模型，并得到深度神经网络
2. 读取图片、视频我
3. 将图片转成张量，送入深度神经网络
4. 进行分析，并得到结果

'''
'''
导入模型API

readNetFromTensorflow
readNetFromCaffe
readNetDarknet,YOLO
readNet -- 会根据不同的模型读取不同的网络

导入模型API参数

readNetFromTensorflow(model,config)
readNetFromCaffe/Darknet(config,model)
readNetFrom(model,[config,[framework]])

读取图片并转换为张量

API

blobFromImage(
image,
scalefactor =1.0,//图像缩放比例
size=Size(),//图像大小
mean=Scalar(), //是一个RGB的三元组，作用是消除图像中光照的变化，给定的RGB 均值是103 116 123 
swapRB=false, //图像中的RB是否交换，对于OpenCV 来说图像是RGB 对于深度学习的模块来说可能是RGB 也可能BGR 默认不交换
crop = false ... //是否对图片进行裁剪。超出模型的大小是否裁剪，默认是不裁剪

)

mean的含义

('./public/images/059-mean的含义.png')
主要减少光照的影响


将张量送入网络并执行

net.setInput(blob)
net.forward()

[实战，物体分类]

'''


# from cv2 import dnn_ClassificationModel as dc
# 1.导入模型，创建神经网络
# 2.读取图片，转成张量
# 3.将张量输入到网络中，并进行预测
# 4.得到结果进行显示

config = ''
model = ''

net = dnn.readNetFromCaffe(config, model)
img = cv2.imread('./public/images/coins.webp')
blob = dnn.blogFromImage(img, 1.0, (224, 244), (104, 117, 123))
net.setInput(blob)
r = net.forward()  # r是人类不可读的

# 读入类别目录

classes = []
path = ''
with open(path, 'rt') as f:
    classes = [x[x.find(" ")+1:] for x in f]


order = sorted(r, reverse=True)

z = list(range(3))
for i in range(0, 3):
    z[i] = np.where(r[i] == order[i][0][0])
    print('第', i+1, '项匹配', classes[z[i]], end='')
    print('类所在行：', z[i]+1, '可能性', order[i])
