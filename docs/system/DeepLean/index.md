---
lang: zh-CN
title: 深度学习
description: 深度学习
---

# 深度学习


## 深度学习流程

[视频来源-B站](https://www.bilibili.com/video/BV1FT4y1E74V/?p=3&spm_id_from=pageDriver&vd_source=010173c6f35c758e74dd6593e5722af0)
[课程](https://www.coursera.org/learn/neural-networks-deep-learning#instructors)

<iframe src="/pdf/Deeplearning深度学习笔记v5.6.pdf" width=780 height =780></iframe>



# 深度学习基本概念

标准神经网络 SNN
图像：卷积神经网络 CNN
一维序列数据例如音频，视频，英语，中文等都是一个字一个字组成：递归神经网络 RNN
无人驾驶：混合神经网络

人类先理解非结构化数据再而了解结构化数据
机器先理解结构化数据再而学习非结构化数据

# 正向传播 反向传播 还有算法的实现以及如何高效地实现神经网络

## 2.1 2.2逻辑回归-二分分类 算法

logistic regression
一张图片 64 *64
64x64 像素值
输入的特征向量x总维度= n小x 64x64x3=1288  即n 小x =[255 ->211->125->100->263->...->64] 总共64*64*3个元素 直接用n表示

二分分类法中
用 x 作为输入的特征总向量 ，用y预测输出的结果标签y 是1 还是 0
用一对（x,y）表示一个单独的样本
x 是特征向量的一个，y 预测输出的结果标签y 是1 还是 0
训练集由m或者m_train个训练样本构成

测试集样本数量 则为m_test
训练集用大写X 表示矩阵 [ x1(代表一列),x2,x3。。。]所以有多少个训练样本就有多少列，n(下坐标)x 表示矩阵的高度
即 X = nx * m 的矩阵

训练样本作为行向量堆叠，构建

x.shape 表示 X 是一个nx * m的矩阵

训练结果是 Y 矩阵=[y1,y2,....,ym]
表示一个1*m的矩阵
Y.shape=(1,m)
014-sigmoid(z).png
![](/images/system/DeepLean/014-sigmoid(z).png)

015-逻辑回归模型.png
![](/images/system/DeepLean/015-逻辑回归模型.png)

016-逻辑回归函数.png
![](/images/system/DeepLean/016-逻辑回归函数.png)

## 2.3 logistic 回归损失函数

为了训练 逻辑回归模型的参数 w 以及 b
需要定义一个成本函数
损失函数 （单个训练样本）-> 成本函数（总体训练样本）凸函数

梯度下降法 实现 成本函数
w ：= w-xxx
表示更新w

## 2.8使用计算图求导

好，所以在程序里是dvar表示导数，你关心的最终变量J的导数，有时最后是𝐿，对代码中各种中间量的导数，所以代码里这个东西，你用􀀂􀀁表示这个值，所以dv = 3，你的代码表示就是da = 3。

前向：计算函数
后向：计算偏导数
sigmoid函数
![](/images/system/DeepLean/017-sigmoid函数.png)

单个样本函数
![](/images/system/DeepLean/018-几个重要函数.png)

梯度下降法简单来说就是一种寻找目标函数最小化的方法。
![](/images/system/DeepLean/019-逻辑回归和梯度下降法.png)

## 2.10 m个样本的梯度下降
向量化技术摆脱for循环


# 单隐层神经网络，所有必须地关键词

# 多层神经网络
