'''
装饰器其实也是一种闭包,其功能就是在不破坏目标函数原有的代码和功能的前提下,为目标函数增加新功能


'''

# 在方法前后执行  额外功能


def sleep():
    import random
    import time
    print("睡眠中")
    time.sleep(random.randint1,5)


# 装饰器的一般写法

def outer(func):
    def inner():
        print("我要睡觉了")
        func
        print("我要起床了")
    return inner
fn=outer(sleep)
fn()

# 装饰器的快捷写法

@outer
def sleep2():
    print("睡觉中2222")


sleep2()