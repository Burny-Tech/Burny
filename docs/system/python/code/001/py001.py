# 列表 list
## 列表的定义，可以包括不同数据，规范：在逗号后有空格
name_list = ['小明', 3, True, ['列表嵌套']]
name_list.pop(0)
name_list.append('小李')
print(name_list)
## 定义空列表
name_list =[]
name_list=list()

## 列表的下标
## 从左往右
# 0,1,2,3 ...
##从右往左
#... ,-3,-2,-1
# num= name_list[100] # 超过下标范围会报错
#  IndexError: list index out of range
##取出嵌套列表的数据
name_list = [[1 , [1, 2, 3]]]
num = name_list[0][1][2]
print(num) # 3

## 列表常用方法

name_list = [1, 2, 3]

## 查询某元素的下标值

print("aa", name_list.index(3)) # aa 2

## 修改特定下标索引的值
name_list[0] = 999
print("aa", name_list[0] )

## 插入  参数：元素下标值，要插入的内容
name_list.insert(1, "小明")

## 在最后追加
name_list.append('小红')

## 在最后追加一批,逐个将name_list2的元素追加到name_list后面，而不是将整个list2 作为一个整体整体追加
name_list2 = ['aa','bb']
name_list.extend(name_list2)
print(name_list)

## 删除
## del 列表[下标索引值]
## 列表.pop(下标)
## 列表.remove("这是一个将被删除的元素") 指定元素删除 从左到右 第一个符合的被删除，如果右两个符合条件的，第二个不会被删除
## list.clear() 清空列表内容

del name_list[2]

## result 的值是 下标为2 的值，而不是列表的值
result = name_list.pop(2)

name_list.remove('小明')

## 统计列表内元素的个数
name_list.extend(["小明", "小明"])
result = name_list.count("小明")

## 统计列表内的个数
result = len(name_list)

## 元素转置
name_list.reverse()
print(name_list)





""" 
list 特点
可以容纳不同类型
数据有序
允许重复
可以修改

"""
## 列表的循环

for name in name_list:
    print(name)





# 元组 tuple
## 元组一旦当完成定义，就不可修改
## 有序，任意数量元素，各元素数据type 可不一样，允许重复元素
## 元组定义格式
## 定义元组字面量
## (元素  , 元素 ,)
"""

变量名称 =  (元素  , 元素 ,)
定义空元组
变量名称 = ()
变量名称 = tuple()

定义单个元素的元组

"""
# 字符串
name_tuple = ("小明")
# 元组
name_tuple = ("小红" , )
name_tuple = ()
# 计算元素的个数
num = len(name_tuple)




# 字符串 str

## 字符串操作

## 字符串也是一个只读的容器

str1 = "abcdefdfefefdsa"

## 分割
str_list =str.split("fe")
print(str_list)

## 去除前后的空格回车符
str1 = ' abb  \n'
str_new =str1.strip()
print(f"str_new:{str_new}")


## 序列切片

## 从序列中取出子序列即切片


"""
序列[起始下标:结束下标：步长]

结束下标(不含)表示何处结束，可以留空，留空视为截取到结尾

序列操作不会影响序列本身，会得到一个新的序列

"""
name_list =[0,1,2,3,4,5,6,7,8,9,10]
# 步长为1，从1开始取，到下标为4(不含下标4)
name_list[1:4]
# 跟原来的name_list一样的
name_list[:]
# 步长为4 ，
name_list[::4]
# 从后往前取
name_list[::-1]









# 集合 set

## 无序，

## 集合为 { }


a = {8, 9, 8}
b = {9, 10, 11, 9}
# 空集合 注意空集合 没有  {} {}是代表字典
empty =set()
## a集合和b 集合 合并
a.union(b)
## 差集
result = a.difference(b)
## 集合a 去掉差集两个集合的差集的内容
a.difference_update()


#a.discard()

## 返回集合的交集

a.intersection()
## 返回集合的交集 并将a 设置为交际
#a.intersection_update()

#a.isdisjoint()
#a.issubset()
#a.issuperset()
#a.update()
#a.symmetric_difference()
#a.symmetric_difference_update()




# 字典 dict


## 字典的定义

## 字典和集合 同样 也是用 大括号 但是不同的是存储的元素是一个个的键值对
## 如果有重复的key ,则后面的key会覆盖前面的key

name_dict = {1: 3, 2: 3, 3: 3, 4: 40, 1: 20}

name_dict={}
name_dict=dict()






## 字典的相关操作


tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del tinydict['Name']  # 删除键 'Name'
tinydict.clear()  # 清空字典
del tinydict  # 删除字典

# dict.items()

# !/usr/bin/python3

tinydict = {'Name': 'Runoob', 'Age': 7}

print("Value : %s" % tinydict.items())
## 以上实例输出结果为：

## Value: dict_items([('Age', 7), ('Name', 'Runoob')])

##Python 字典 update() 函数把字典参数 dict2 的 key/value(键/值) 对更新到字典 dict 里。
## dict.update(dict2)

# !/usr/bin/python3

tinydict = {'Name': 'Runoob', 'Age': 7}
tinydict2 = {'Sex': 'female'}

tinydict.update(tinydict2)
print("更新字典 tinydict : ", tinydict)
# 以上实例输出结果为：

#更新字典
## tinydict: {'Name': 'Runoob', 'Age': 7, 'Sex': 'female'}

## 遍历

## for循环的两种方式
tinydict_key = tinydict.keys();
for i in tinydict_key:
    print(i)
    print(tinydict[i])

for key in tinydict:
    print(key)
    print(tinydict[key])


# 字典不支持下标索引



# 容器的通用操作

# 长度，最大的元素，最小的元素
#len(name_list)
#max(name_list)
#min(name_list)


# 类型转换 容器转列表
contain1 = "str"
contain2 = ['str','abc']
contain3 = ('str','efg')
contain4 = {'a','b'}
contain5 = {1:3,2:3,3:3}
print(f"转换结果为:{list(contain1)}")
print(f"转换结果为:{list(contain2)}")
print(f"转换结果为:{list(contain3)}")
print(f"转换结果为:{list(contain4)}")
print(f"转换结果为:{list(contain5)}")

"""
转换结果为:['s', 't', 'r']
转换结果为:['str', 'abc']
转换结果为:['str', 'efg']
转换结果为:['b', 'a']
转换结果为:[1, 2, 3]
"""

# 类型转换 容器转元组
print(f"转换结果为:{tuple(contain1)}")
print(f"转换结果为:{tuple(contain2)}")
print(f"转换结果为:{tuple(contain3)}")
print(f"转换结果为:{tuple(contain4)}")
print(f"转换结果为:{tuple(contain5)}")

"""
转换结果为:('s', 't', 'r')
转换结果为:('str', 'abc')
转换结果为:('str', 'efg')
转换结果为:('b', 'a')
转换结果为:(1, 2, 3)

"""

# 类型转换 容器转字符串
print(f"转换结果为:{str(contain1)}")
print(f"转换结果为:{str(contain2)}")
print(f"转换结果为:{str(contain3)}")
print(f"转换结果为:{str(contain4)}")
print(f"转换结果为:{str(contain5)}")

"""
看着像各自的类型，其实已经是字符串了
"转换结果为:['str', 'abc']"
"转换结果为:('str', 'efg')"
"转换结果为:{'b', 'a'}"
"转换结果为:{1: 3, 2: 3, 3: 3}"
"""

# 类型转换，容器转集合
print(f"转换结果为:{set(contain1)}")
print(f"转换结果为:{set(contain2)}")
print(f"转换结果为:{set(contain3)}")
print(f"转换结果为:{set(contain4)}")
print(f"转换结果为:{set(contain5)}")


# 容器通用排序功能

#
# sorted(容器,[reversed])
# 排序完之后变成列表
print(f"排序转换结果为:{sorted(contain1)}")
print(f"排序转换结果为:{sorted(contain2)}")
print(f"排序转换结果为:{sorted(contain3)}")
print(f"排序转换结果为:{sorted(contain4)}")
print(f"排序转换结果为:{sorted(contain5)}")


"""
排序转换结果为:['r', 's', 't']
排序转换结果为:['abc', 'str']
排序转换结果为:['efg', 'str']
排序转换结果为:['a', 'b']
排序转换结果为:[1, 2, 3]

"""

# 字符串比较大小

