"""

当需要大量创建一个类的实例对象是,可以使用工厂对象

即 从原生的使用类的构造去创建对象的形式,
迁移到
基于工厂提供的方法去创建对象的形式
"""

class Person:
    pass


class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

p1 =Worker()
p2 =Student()
p3 = Teacher()


# 工厂模式

'''

大批量创建对象的时候有统一的入口,易于代码维护
当发生修改,仅修改工厂类的创建方法即可

符合显示世界模式,即由工厂来制作产品,对象


'''

class Person:
    pass
class Worker(Person):
    pass
class Student(Person):
    pass
class Teacher(Person):
    pass

class Factory:
    def get_person(self,type):
        if type == '1':
            return Worker()
        elif type == '2':
            return Student()
        else:
            return Teacher()


factory= Factory()
w1 = factory.getPerson("1")
w2 = factory.getPerson("2")
w3 = factory.getPerson("3")

