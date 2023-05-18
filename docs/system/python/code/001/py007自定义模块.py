# 自定义一个文件就是一个模块
import py004

from py004 import test_func

## 注意事项

# 导入多个模块同名模块

# 后引入的同名模块会覆盖掉先导入的


# __main__ 变量
from py004 import test_func
# 本文件导入但是没有使用 test_func，如果运行本文件，会执行py004 里面已经写好的test_func 函数
# 只有当程序是直接执行的才会进入if 内部，如果是被导入的，则无法进入




# __all__ 变量 演示

"""
py0071 中
只显示地导出 testA 函数，没有导出test B函数

如果在py0072 中使用

from py0071 import *
则只能使用testA() 函数，不能使用testB函数

—__all__  变量 只能限制使用 *  的时候导入

如果采用
from py0071 import testB
则可以调用testB函数

"""


