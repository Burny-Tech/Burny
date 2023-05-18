# 类定义
class Student:
    name = None
    gender = None


# 创建对象
stu1 = Student();

# 对象的属性赋值
stu1.name = 'xiaohong'
stu1.gender = 'sex'

print(stu1)  # <__main__.Student object at 0x0000018FEEFD52A0>

# 类的成员变量 类的行为，即定义在类中的函数  又称 类的成员变量
"""

## 注意区分 函数 方法 俗称
### 函数：写在类外面的方法

### 方法：写在类里面的方法


在类中定义成员方法和定义函数基本一致，但仍有细微区别

def 方法名(selft ,形参1,...形参N)
    方法体

可以看到，在方法定义的列参中，有一个self关键字

self 关键字是成员方法定义的时候 ，必须填写的。

* 它用来表示类对象自身的意思
* 当我们使用类对象调用方法的时候，self 会自动被python 传入
* 在方法内部，想要访问类的成员变量，必须使用 self

"""


class Teacher:
    name = None
    age = None

    def tech(self):
        print("我是一名老师")
        print(self.name)
        print(self.age)

    def tech(self, msg):
        print(f"你说{msg}")


te = Teacher()
# 注意调用，te.tech
te.tech
te.tech(msg="有参数")

"""
不能写同名的方法
"""

# 构造方法： __init__() 方法称为构造方法
"""
可以实现
在创建类对象的时候，会自动执行
在创建对象的时候，将传入参数自动传递给__init__方法使用

"""


class User:
    name: None
    age: None
    tel: None

# ERROR 错误写法
    # def __init__(self, name, age):
    #     self.name = name
    #     self.age = age

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel


# ERROR 错误写法
# user1 = User(name="小红", age=18)
user2 = User(name="小白",age= 18,tel= 15999999)

# print(user1)
print(user2)

"""
Traceback (most recent call last):
  File "D:\burny\gitclone\qianyi\Burny.tech\docs\system\python\code\002\py0021类.py", line 94, in <module>
    user1 = User(name="小红", age=18)
TypeError: User.__init__() missing 1 required positional argument: 'tel'
<__main__.Student object at 0x0000018A7953FFD0>

"""