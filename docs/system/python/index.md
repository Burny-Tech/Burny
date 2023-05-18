## Python 安装

[官网](https://www.python.org/downloads/windows/)

下载安装即可

 验证是否安装成功

python 现在需要3.10版本以上即可

```python
在cmd中直接输入
python有显示版本号就是可以的。
```



## P7 Hello world

```python
"""
在cmd中输入python 
后直接输入
"""
print("Hello world")
"""
输入
exit() 
可退出，注意需要添加双括号
"""
```

## P10

```python
"""
在cmd中
可以python xxx.py 文件
执行python文件
"""


shift+alt+上/下 将当前文件上移或者下移
ctrl+shift+f10 运行当前文件
shift+f6 重命名文件

```

## P14 数据类型

数据类型

| Number          | int<br />float<br />complex<br />bool | 整数<br />浮点数<br />复数不常用<br />布尔值 |
| --------------- | ------------------------------------- | -------------------------------------------- |
| string          | 字符串                                |                                              |
| List 列表       | 有序的可变序列                        |                                              |
| Tuple 元组      | 有序的不可变序列                      |                                              |
| Set 集合        | 无序不重复的集合                      |                                              |
| Dictionary 字典 | 无序 键值对                           |                                              |







## P15 注释

```python

# 单行注释  # 号后加空格 规范

"""
多行注释
多行注释
"""
```



## P16 变量

```python

# 定义变量

# 变量名  = 变量值

a = 5
b = "string"

# 字符串连接 中间 可以用 ，
print("aaa",a,"元")

# 查看数据的类型
# 区别于变量类型  和数据的类型  变量是没有类型之说的

print(type(a))

# 字符串变量 表示 变量存储了字符串而不是表示变量就是字符串

```



## P18 数据类型转换

```python
int(x)     # 将x转为一个整数
float(x)   # 将x转为一个浮点数
str(x)     # 将x 转为一个字符串
```

## P19 标识符

标识符

* 变量名字
* 方法名字
* 类名字等

  

命名规范：

* 包名：全部小写字母，中间可以由点分隔开，不推荐使用下划线。
* 模块名：全部小写字母，如果是多个单词构成，可以用下划线隔开，如dummy_threading
* 函数名应该为小写，可以用下划线风格单词以增加可读性。如：myfunction，my_example_function
* 类名：总是使用首字母大写单词串。如MyClass。内部类可以使用额外的前导下划线
* 异常名：异常属于类，命名同类命名，但应该使用Error作为后缀。如FileNotFoundError
* 变量名：变量名：全部小写，由下划线连接各个单词。如color = WHITE，this_is_a_variable = 1



* 不论是类成员变量还是全局变量，均不使用 m 或 g 前缀
* 私有类成员使用单一下划线前缀标识，如_height。多定义公开成员，少定义私有成员
* 总使用“self”作为实例方法的第一个参数。总使用“cls”作为类方法的第一个参数

## P20 算法运算

```python

2**2  =4   2的2次方
9//2  =4   9整除2 


# 复合赋值运算符

+=
-=
*=
/=
//=
%=
**=


```



## P21 字符串

### 字符串定义

```python

# 单引号
str = '我是一个字符串'
# 双引号
str = “我是一个字符串”
# 模板字符串
str= """
我是一个字符串，并且是一个模板字符串
我在这里面换行就是换行

"""


```

### 字符串的拼接



注意：字符串无法和非字符串类型进行拼接

```python
a="我是一个字符串"
b="我也是一个字符串"
# 方式一 通过 + 号
print(a+b)
print(a,b)



```

### 字符串格式化

```python

message  = "%s    %s" %("我这句话是对的",68)
print(message)

# 结果输出：
我这句话是对的    68

```



```python

%s  将内容转换为字符串，放入占位位置
%d  将内容转换为整数，放入占位位置
%f  将内容转换为浮点数，放入占位位置

```



```python
# 格式化方式二

"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
"{0} {1}".format("hello", "world")  # 设置指定位置
"{1} {0} {1}".format("hello", "world")  # 设置指定位置
    
  #   如果在字符串中需要直接展示花括号，则用另一个花括号包裹起来转义
     "{{我是谁}}:{}".format("皮卡丘")
```



```python

# 格式化方式三

# 此种方式不会对数字进行精度化

name ="chen"
year = 2005
month = 6

result  = f"我是{name},今年是{year}"

print(result)
```



### 对表达式进行格式化 

```python



# 表达式：一条具有明确执行结果的代码语句

# 例如：

print("2*6的结果是：%d" %(2*6))
print(f"2*6的结果是：{2*6}")
print("字符串在python中的类型是：%s" % type("python"))

# 输出结果

2*6的结果是：12
2*6的结果是：12
字符串在python中的类型是：<class 'str'>
```





###  字符串格式化-数字宽度控制

```python



 
# 用 m.n
# m 表示控制的宽度，要求是数字，设置的宽度小于数字本身，不生效
# n 表示小数点的精度，要求是数字，会进行小数的四舍五入

# 例如
"""
%5d 表示将整数的宽度控制在5位，如数字11 北设置为5d ,就会变成 [空格][空格][空格]11 ,用三个空格补足宽度
%5.2f 表示将宽度控制为5，将小数点精度设置为2
小数点和小数部分也算入宽度计算 如 11.345 设置了%7.2f 后，结果是  [空格][空格]11.35    2个空格补足宽度，小数部分限制2位精度后，四舍五入为.35
%.2f 11.345 -> 11.34


"""
```



## 输入函数

```python
print("请输入数据")
data = input()
print(f"您输入的是{data}")

上面三句等同于下面两句

data = input("请输入数据")
print(f"您输入的是{data}")


# 结果窗口

请输入数据66
您输入的是66

```



## 流程 if-else

```python

# python 对空格格数有非常严格的校验
# 代码块里面为4个空格

if 1 >= 2:
    print("ss")
elif 6<=3 :
    print("永远不会输出")
else:
    print("dd")
https://www.bilibili.com/video/BV1qW4y1a7fU?p=36&spm_id_from=pageDriver&vd_source=010173c6f35c758e74dd6593e5722af0
```

## 流程 while

```python

while True:
    print("永远执行")
```

## 流程 for



```python

# 语法
# 注意空格缩进

for 临时变量 in 待处理数据集(序列)
	循环满足条件时的代码

```

#### range 语句

序列类型是指，其内容可以一个个依次取出的一种类型，包括字符串，列表，元组等



| range(num)            | 从0开始，到num结束的数字序列（不含num本身）                  | num(5)-> [0,1,2,3,4]  |
| --------------------- | ------------------------------------------------------------ | --------------------- |
| range(num1,num2)      | 从num1,开始，到num，结束的数字序列（不含num本身）            | range(1,4)->[1,2,3]   |
| range(num1,num2,setp) | 从num1,开始，到num，每次递增step.到结束的数字序列（不含num本身） | range(1.9,3)->[1,4,7] |
|                       |                                                              |                       |

## 循环中断

```python
continue : 暂时跳过某次循环，直接进行下一次
break :提前退出循环，不再继续；break 只在break 所在的最里面的for循环中提前退出循环，若外层还有for循环，外层循环不受break影响，

```



## 容器

@[code](./code/001/py001.py)





## P51 函数

```python
函数执行从上往下执行

def 函数名 (传入参数)：
	函数体
    return 返回值

声明函数的时候,传入参数称为：形式参数
调用函数的时候,传入参数称为：实际参数


函数返回为空 可用 return None
效果等同于不写return语句
```



### 函数说明文档

```python
def func(x,y):
    """
    :param x: 形参x的说明
    :param y：形参y的说明
    :return: 返回值说明
    """
    函数体
    return "A"

```

### 变量的作用域

```python
# 局部变量
# 作用于函数体内部

# 全局变量
# 在函数外部定义即为外部变量

num=20 #全局变量
def test_a():
    l= 10  # 局部变量
    num=10  # 局部变量，虽然与外部变量标识符一样，修改了num不会修改外部的num变量，如果要修改需要加上global 关键字
    global num = 10 # 会将外部num = 20 更改为num 10

# 如果在函数内部将全局变量设置为

```





### 函数多返回值



```python

# 如果一个函数要有多个返回值

def test_return():
    return 1, 2

x, y = test_return()
print(x)
print(y)
```







### 函数多种传参方式

@[code](./code/001/py003.py)



### 匿名函数

@[code](./code/001/py004.py)



https://www.bilibili.com/video/BV1qW4y1a7fU?p=84&spm_id_from=pageDriver&vd_source=010173c6f35c758e74dd6593e5722af0





## 异常与包

@[code](./code/001/py005异常.py)

### 模块

@[code](./code/001/py006模块.py)



@[code](./code/001/py007自定义模块.py)

### 包



@[code](./code/001/py008包.py)

@[code](./code/001/py008/__init__.py)

@[code](./code/001/py008/py0081.py)

@[code](./code/001/py008/py0082.py)

## JSON



@[code](./code/001/py009JSON.py)





## 类 对象



类 对象 变量 方法(成员方法)

@[code](./code/002/py0021类.py)



















