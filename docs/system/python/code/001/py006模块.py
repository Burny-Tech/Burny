# 模块能定义函数，类和变量，
# 导入语法
# [from 模块名] import [模块 |类 | 变量|函数 |*] [as 别名]
# 常用的组合如下
"""
import 模块名
from 模块名 import 类变量方法等
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名
"""

# 基本语句

"""
import 模块名
import 模块名1,模块名2

模块名.功能名()  # 可以使用模块内部的全部功能(类、函数、变量)
"""
import  time
time.sleep(10)

import  time as t

t.sleep(10)

"""
from 模块名 import 功能名 as 别名 # 只导入模块中的一个功能
"""

from time import  sleep
from time import sleep as sl
sleep(1)
sl(10)

# 导入模块里面的所部功能，并且可以直接使用
from time import  *

sleep()
