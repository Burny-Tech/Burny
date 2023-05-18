"""
内置的类方法，各自有特兹特殊的功能
这些内置的方法称为 魔术方法

主要的魔术方法

构造函数

__init__

__str__

__lt__ 只能用 > 或者小于

__le__ 只能用 >=或者 <=



__eq__ 重要 判断是不是同一个对象

"""


# 字符串魔术方法

class Student2:
    name = None
    age = None

    def ss(self):
        print("ss")

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name ={self.name} ,age ={self.age}"

    def __lt__(self, other):
        return self.age < other.age


stu = Student2("小红0", 22)

print(str(stu))  # name =小红0 ,age =22

stu2 = Student2("小白", 23)

print(stu < stu2)


# 对象的三大特性：封装  私有成员变量 ，私有成员方法  以两个下划线表示


class Phone:
    __IMEI = None
    name = None

    # 私有成员方法
    def __printA(self):
        print("私有成员方法")

    def get(self):
        print("类内部调用")
        self.__printA()
        print("t")


phone = Phone()
phone.get()


# 对象的三大个性：继承

class smallPhone(Phone, Student2):  # 括号里继承 ,单继承 多继承
    pass  # 表示继承了，但不想添加新功能


## 复写父类的方法 复写父类的变量
class bigPhone(Phone, Student2):
    name = '小红'  # 直接复写父类的成员

    def get(self):  # 直接复写父类的方法
        print("复写父类的方法")


## 调用父类的成员
"""
调用方式1
使用成员变量：父类名.成员变量
使用成员方法: 父类名.成员方法(self)

调用方式2
super.成员变量
super.成员方法()
"""


class XPhone(Phone, Student2):

    def xx(self):
        print(Student2.name)
        Student2.ss(self)

        print(super().name)
        super().get()

##Python在3.5之后进行添加的 变量的类型注解 函数和方法类型的注解
## 是一种规范，注释，备注，不是一种强制性的，仅仅给代码提示的功能而已。

## 功能：明确类型，pycharm 有提示等

## 调用方法，进行传参  ctrl+p 提示传参

## 变量:类型

a:int=10  # 变量a 为整形
b:float = 100.0
c:str ="fs"
f:list=[1,2]
f:list[int] =[11,22]
f:list[str] =["aaa0","bbb"]
f:tuple
f:set
f:dict[str,str]={"a": "b",1: 2}  # 提示，key value 都是str,但不一定要是str ,其他也是也是可以运行的
f:bool

stu = Student2()

## 第二中写法，不推荐在后面进行注释
## 变量=数据 # type:类型
a =10 # type:int

def A():
    return  "a"

b:str =A()


## 变量:类型   -> 函数返回值注解
def B(data:int) -> str:
    return "返回值为字符串"

B(data = 5)

## Union联合类型

from typing import Union
# 可以是字符串，也可以是我整型
mylist:list[Union[str,int]] = [1,2,"zifuchuan"]

# 入参 data 可以是字符串，也可以是整形，
# 返回值 可以是整形，也可以是float
def C(data:[Union[str,int]]) ->Union[int,float]:
    pass






# 对象的三大特性： 多态


class Animal:
    def speak(self):
        pass  # 可表示一个抽象方法
class Dog:
    def speak(self):
        print("dog")
class Cat:
    def speak(self):
        print("cat")

def make_nose(animal:Animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_nose(dog)
make_nose(cat)
