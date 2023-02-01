# 图像合并的步骤
'''
读文件并重置尺寸
根据特征点和计算描述子,得到单应性矩阵
图像变换
图像拼接并输出图像
'''

'''
坐标系
此坐标与之前的坐标不同,

('./public/images/034-坐标系.png)

('./public/images/035-图像拼接原图.png)
('./public/images/036-图像拼接结果.png)
('./public/images/037-单应性矩阵变换.png)
('./public/images/038-单应性矩阵变换.png)
('./public/images/039-放大窗口.png)
('./public/images/040-图像平移.png)
('./public/images/041-图像平移.png)

'''

# 找特征点，描述子，计算单应性矩阵




import cv2
import numpy as np
def get_home(img1, img2):
    # 创建特征转换对象
    sift = cv2.SIFT_create()
    # 通过特征点转换对象获得特征点和描述子
    k1, d1 = sift.detectAndCompute(img1, None)
    k2, d2 = sift.detectAndCompute(img2, None)
    # 创建特征匹配器
    bf = cv2.BFMatcher()
    # 进行特征匹配
    # k 值,代表选取最匹配的k个点
    match = bf.knnMatch(d1, d2, 2)
    # 过滤特征,找出有效的特征匹配点,过滤阈值 0.7 或 0.8

    verify_ratio = 0.8
    # 有效特征点
    verify_matches = []
    for m1, m2 in match:
        # 如果之间的距离 小于 0.8 说明准确率越高.大于0.8 ,说明准确率越低
        if m1.distance < 0.8 * m2.distance:
            verify_matches.append(m1)
    # 计算单应性矩阵
    # 进行单应性矩阵 的有效特征点必须 大于 8个点.
    min_matches = 8

    if len(verify_matches) > min_matches:
        # img1 坐标点 和img2 的坐标点
        img1_pts = []
        img2_pts = []
        for m in verify_matches:
            # 添加第一张图片的特征点对应的图标
            img1_pts.append(k1[m.queryIdx].pt)
            img2_pts.append(k2[m.queryIdx].pt)
            # 对坐标点进行重新定义,更换格式符合计算单应性矩阵的格式
            # [(x1,y1),(x2,y2),...]
            # [[x1,y1],[x2,y2],...]
            # x 是
        img1_pts = np.float32(img1_pts).reshape(-1, 1, 2)
        img2_pts = np.float32(img2_pts).reshape(-1, 1, 2)

        H, mask = cv2.findHomography(img1_pts, img2_pts, cv2.RANSAC, 5.0)
        return H
    else:
        print('error : 没有足够的特征匹配点')
        exit()

# 图像拼接


def stitch_image(img1, img2, H):
    # 获得每张图片的四个角点 逆时针
    # 获得高度,宽度
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]
    # 转换为浮点型,转为3维
    # 第一个值 x  设置为 -1 ,任意值
    # 第二个值 y  有一列
    # 第三个值  每个y 有2个值,
    img1_dims = np.float32(
        [[0, 0], [0, h1], [w1, h1], [w1, 0]]).reshape(-1, 1, 2)
    img2_dims = np.float32(
        [[0, 0], [0, h2], [w2, h2], [w2, 0]]).reshape(-1, 1, 2)
    # 对图片1进行变换,目的是有角度的拼接,类似于投影变换
    # img1_transform  如果为负值 ,则代表不显示
    img1_transform = cv2.perspectiveTransform(img1_dims, H)
    # 将图形1 和图形2 进行拼接    axis 0 横向拼接,  .
    result_dims = np.concatenate((img2_dims, img1_transform), axis=0)
    # 计算x ,y最大值和最小值
    # 二维变成一维 ,四舍五入
    [x_min, y_min] = np.int32(result_dims.min(axis=0).ravel()-0.5)
    [x_max, y_max] = np.int32(result_dims.min(axis=0).ravel()+0.5)

    # 得到平移后的举例
    transform_dist = [-x_min, -y_min]

    # 平移后的图片
    # ('./public/images/042-对图1进行平移.png')
   #  result_img = cv2.warpPerspective(img1, H, (x_max - x_min, y_max - y_min))

    # 将图2 平移过来
    # 线性代数 矩阵平移 乘以 起始坐标 起始坐标如下.
    # [1,0,dx]
    # [0,1,dy]
    # [0,0,1]
    transform_array = np.array(
        [
            [1, 0, transform_dist[0]],
            [0, 1, transform_dist[1]],
            [0, 0, 1]
        ]
    )
    result_img = cv2.warpPerspective(
        img1, transform_array.dot(H), (x_max - x_min, y_max - y_min))

    # 拼接
    result_img[transform_dist[1]:transform_dist[1]+h2,
               transform_dist[0]:transform_dist[0]+w2] = img2

    return result_img

    # 读取文件,设置成固定的大小
img1 = cv2.imread('./public/images/zheng.png')
img2 = cv2.imread('./public/images/zheng.png')

img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

# 横向拼接图片
inputs = np.hstack((img1, img2))

# 找特征点,描述子,计算单应性矩阵，此功能比较单一，写成函数

H = get_home(img1, img2)

# 根据单应性矩阵对图像进行变换,然后平移到大的图像,再平移

result_img = stitch_image(img1, img2, H)


# 拼接并输出最终结果
cv2.imshow('img', inputs)

cv2.waitKey(0)
