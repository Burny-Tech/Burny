class Tool:
    pass

t1  = Tool()
t2 = Tool()

print(t1)
print(t2)

'''
<__main__.Tool object at 0x000002487BDB4B80>
<__main__.Tool object at 0x00000248734346D0>

定义:保证一个类只有一个实例,并提供一个访问它的全局访问点
场景: 当一个类只能有一个实例,而客户可以从一个众所周知的访问点访问它时.

步骤一 在一个文件中定义如下代码
class StrTools:
    pass
    
str_tool =StrTools()

步骤二

from test import str_tool
s1 = str_tool
s2 = str_tool
print(s1)
print(s2)




优点:
节省内存
节省创建对象的开销







'''