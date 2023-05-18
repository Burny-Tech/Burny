"""



从物理上看，包就是一个文件夹，在该文件夹包含了一个 —__init__.py 文件，该文件夹可用于包含多个模块文件

!!!!!    文件夹下如果有 ————init__.py 的话就是一个包，如果没有的话就是一个普通的文件夹

从逻辑上看，包的本质依然是模块

包的作用：
当我们的包文件越来越多时，包可以帮助我们管理这些模块，包的作用就是包含



"""

# 四种导入方式

from py008.py0081 import testA

from py008.py0082 import testB

from py008 import py0081
from py008 import py0082

import py008.py0081
import py008.py0082

testA()
testB()

from py008 import py0081,py0082


# 安装第三方包

"""
科学计算：numpy
数据分析： pandas
大数据： pyspark apache-flink
图形化: matplotlib 、pyecharts
人工智能： tensorflow
"""

"""
安装第三方包

cmd命令行中

pip install numpy

网速慢可用以下方法，-i 是指下载的地址，国内镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple  numpy

也可以在pycharm 中中的设置 - 项目 ：python 解释器


查看安装的第三方包

pip list 


"""